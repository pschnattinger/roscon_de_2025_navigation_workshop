# syntax=docker/dockerfile:1.6

# Default to ROS Jazzy so `docker build` works without args
ARG ROS_DISTRO=jazzy
FROM ros:${ROS_DISTRO}

ENV DEBIAN_FRONTEND=noninteractive

# Use bash with pipefail for safer RUNs
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Base tooling for adding repos + TLS
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl gnupg ca-certificates lsb-release && \
    rm -rf /var/lib/apt/lists/*

# Add OSRF Gazebo apt repository (keyring-based, no sudo/apt-key)
RUN set -euo pipefail; \
    ARCH="$(dpkg --print-architecture)"; \
    CODENAME="$(. /etc/os-release && echo "${UBUNTU_CODENAME}")"; \
    mkdir -p /etc/apt/keyrings; \
    curl -fsSL https://packages.osrfoundation.org/gazebo.gpg | gpg --dearmor -o /etc/apt/keyrings/gazebo-archive-keyring.gpg; \
    echo "deb [arch=${ARCH} signed-by=/etc/apt/keyrings/gazebo-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable ${CODENAME} main" > /etc/apt/sources.list.d/gazebo-stable.list

# Install ROS/Gazebo packages
# NOTE:
# - If you're on a ROS/Ubuntu combo that doesn't offer gz-harmonic, swap it for the appropriate Gazebo version.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ros-${ROS_DISTRO}-turtlebot4-simulator \
      ros-${ROS_DISTRO}-rmw-cyclonedds-cpp \
      gz-harmonic \
      # Optional dev/quality-of-life tools (remove to slim)
      python3-colcon-common-extensions \
      less && \
    rm -rf /var/lib/apt/lists/*

# Defaults (can be overridden at build or runtime)
ARG ROS_DOMAIN_ID=0
ENV ROS_DOMAIN_ID=${ROS_DOMAIN_ID} \
    RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Let compose override; otherwise drop into a shell
CMD ["bash"]
