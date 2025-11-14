========================
Introduction to Workshop
========================

This workshop is designed to provide hands-on experience with ROS2 Navigation (Nav2) using the TurtleBot4 platform.

We have 4 TurtleBot4 robots available for practical exercises.

On top of letting the robot drive around we will also look into tooling other than RViz, namely the **Lichtblick Suite** for robot visualization and interaction.

This is especially useful when working with the real robots and restriction and problems manily to middleware related issues.

At NODE Robotics we were facing challenges especially with RMW Middleware and real hardware communication.

Therefore Lichtblick Suitee provides a suitable alternative for monitoring and evaluating live robot data.

The turtlebot4s are running ROS2 Jazzy with FastRTPS as middleware.

The workshop uses latest Nav2 features available in ROS2 Kilted. Therefore we will connect the base system with navigation running in docker containers.


Requirements
================

To follow along with this workshop, you will need:

- A Laptop with ROS2 Dev Container installed preferably with ROS2 Kilted.
- SSH
- Basic knowledge of ROS2 and Nav2
- Basic knowledge of Docker

General Structure
=================

File Structure
---------------
The workshop uses the base system of the Turtlebot4 and a standalone repo which can be found here: `ROSConDE 2025 Navigation Workshop Repo <https://github.com/pschnattinger/roscon_de_2025_navigation_workshop>`_

The turtlebots come with a pre-cloned version of this repository located in ``/home/ubuntu/roscon_de_2025_navigation_workshop/`` on the robot.

Environemts which the robot should operate in are located under ``/home/ubuntu/roscon_de_2025_navigation_workshop/envs/``.

Docker containers
-----------------
The navigation stack and related nodes will be run inside docker containers.

The docker compose file can be found under ``/home/ubuntu/roscon_de_2025_navigation_workshop/turtlebot4_navigation/docker-compose.yaml`` on the robot.
