# Quickstart

This folder provides a Docker-based environment to run the TurtleBot4 Gazebo simulation.

Overview

- A Dockerfile builds an image that installs ROS (default: Jazzy), TurtleBot4 simulator packages and Gazebo.
- `docker-compose.yml` defines a single service (`turtlebot-gazebo`) which can be built locally or pulled from a prebuilt image.
- The container uses CycloneDDS as the default RMW implementation and defaults to `ROS_DOMAIN_ID=0`.

Prerequisites

- Docker and Docker Compose (Compose v2 or higher recommended).
- If you want GPU acceleration: a recent NVIDIA driver and the Docker Engine configured to expose GPUs (nvidia-container-toolkit). If you use GPUs, make sure your Docker/Compose supports the `gpus` option or use `--gpus` with `docker run`.
- X11 support on the host for Gazebo GUI (or use VNC / Xpra if preferred).

Quick start (build + run)

The easiest way to build and run the simulation (builds the image then starts the service):

```bash
docker compose up --build
```

If you only want to run without rebuilding (useful when pulling a prebuilt image):

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d --build
```

Access the container shell (if you prefer to poke around manually):

```bash
# start (detached) first
docker compose up -d --build

# then open a shell in the running container
docker exec -it ros2-turtlebot4-jazzy bash
```

Build options

- The Dockerfile accepts a build-arg `ROS_DISTRO` (default: `jazzy`). Example:

Important environment variables

- `CYCLONEDDS_URI` — CycloneDDS XML used in the container (configured in `docker-compose.yml`).
- `RMW_IMPLEMENTATION` — defaults to `rmw_cyclonedds_cpp` in the compose file and Dockerfile.
- `ROS_DOMAIN_ID` — defaults to `0`. Set this if you need multiple isolated ROS networks on the same LAN.
- `DISPLAY` — forwarded from the host to allow Gazebo GUI; the compose file already maps `/tmp/.X11-unix`.

GPU and GUI notes

- X11: The compose file mounts the X11 socket (`/tmp/.X11-unix`) and forwards `DISPLAY`. On some hosts you may also need to run `xhost +local:root` (or a more secure variant) before starting the container so the container can open windows on your display.
- GPU: If your machine has an NVIDIA GPU, install `nvidia-container-toolkit` and either enable the `gpus: all` option in `docker-compose.yml` or run with `--gpus all`.

Troubleshooting

- Gazebo display doesn't show / complains about connecting to display:
  - Ensure `DISPLAY` is set on the host and `/tmp/.X11-unix` is mounted into the container.
  - Try `xhost +local:root` temporarily to allow the container to connect.
- Permissions errors when accessing hardware devices:
  - The `turtlebot-gazebo` service uses `privileged: true` and `network_mode: host` in the compose file to allow access to host resources. If you removed those for security, you may need to add specific device mappings.
- DDS discovery issues across hosts:
  - If running multiple machines, ensure `ROS_DOMAIN_ID` and the CycloneDDS configuration (interfaces/multicast) are set correctly so participants can discover each other.

Files of interest

- `Dockerfile` — builds the image; accepts `ROS_DISTRO` and `ROS_DOMAIN_ID` build args.
- `docker-compose.yml` — defines the `turtlebot-gazebo` service, environment variables, and runtime options.
- `entrypoint.sh` — container entrypoint (copied into the image and made executable by the Dockerfile).

Example: override ROS_DOMAIN_ID

```bash
# run with a different domain id
ROS_DOMAIN_ID=5 docker compose up --build
```.
