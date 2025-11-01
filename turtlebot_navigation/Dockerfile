# syntax=docker/dockerfile:1.6

# Default to ROS Jazzy so `docker build` works without args
ARG ROS_DISTRO=kilted
FROM ros:$ROS_DISTRO-ros-core

ENV DEBIAN_FRONTEND=noninteractive

# Use bash with pipefail for safer RUNs
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Base tooling for adding repos + TLS
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl gnupg ca-certificates lsb-release \
      ros-${ROS_DISTRO}-rmw-cyclonedds-cpp \
      python3-colcon-common-extensions \
      less\
      python3-colcon-common-extensions \
      python3-rosdep \
      python3-vcstool \
      python3-pip \
      git \
      build-essential

WORKDIR /ws
RUN mkdir -p /opt/roscon

COPY roscon.repos /ws/src/roscon/roscon.repos

RUN vcs import src < /ws/src/roscon/roscon.repos

RUN  /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \
  rosdep init && \
  rosdep update && \
  rosdep install --from-paths . -ry && \
  colcon build --merge-install --install-base /opt/roscon --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF $ADDITIONAL_CMAKE_CONFIG --packages-up-to turtlebot4_navigation"

RUN rm -rf /var/lib/apt/lists/*

# Defaults (can be overridden at build or runtime)
ARG ROS_DOMAIN_ID=0
ENV ROS_DOMAIN_ID=${ROS_DOMAIN_ID} \
    RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Entrypoint
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
