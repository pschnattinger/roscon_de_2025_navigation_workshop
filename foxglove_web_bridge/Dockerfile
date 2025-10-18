# syntax=docker/dockerfile:1.6


# Default to ROS Jazzy so `docker build` works without args
ARG ROS_DISTRO=jazzy
FROM ghcr.io/ros-navigation/nav2_docker:$ROS_DISTRO-1.3.9

ENV DEBIAN_FRONTEND=noninteractive

# Base tooling for adding repos + TLS
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-foxglove-bridge \
    ros-${ROS_DISTRO}-rmw-cyclonedds-cpp \
    ros-${ROS_DISTRO}-slam-toolbox
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["ros2", "launch", "foxglove_bridge", "foxglove_bridge_launch.xml"]
