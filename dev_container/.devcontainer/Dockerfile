FROM cinoderobotics/turtlebot4_navigation:kilted-amd64-v1.1.0

# Set up the user and group, remove the standard user first.
ARG USERNAME=virtual
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ENV DEBIAN_FRONTEND="noninteractive"
RUN sudo userdel ubuntu && sudo rm -r /home/ubuntu
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME
RUN chown -R virtual:virtual /home/virtual

# Set up user access rights.
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Basic system update.
RUN rosdep update
RUN apt update \
    && apt upgrade -y \
    && apt install -y sudo software-properties-common

# Install additional development tools.
RUN apt install -y nano tmux git-cola gitk net-tools qtwayland5

# Install additional ROS tools.
RUN apt install -y ros-kilted-desktop ros-dev-tools ros-kilted-rmw-cyclonedds-cpp ros-kilted-rmw-fastrtps-cpp ros-kilted-plotjuggler-ros

# Needs to be installed as user.
RUN PIP_BREAK_SYSTEM_PACKAGES=1 pip install --user colcon-mixin pre-commit \
    && colcon mixin add default https://raw.githubusercontent.com/colcon/colcon-mixin-repository/master/index.yaml \
    && colcon mixin update

# Switch from root to user.
USER $USERNAME
