================
TurtleBot4 Setup
================

General
=======

The TurtleBot4 is a popular mobile robot platform designed for education and research in robotics.
It is equipped with various sensors and actuators, making it suitable for a wide range of applications, including navigation, mapping, and manipulation.

The TurtleBot4 documentation can be found here: `TurtleBot4 Documentation <https://turtlebot.github.io/turtlebot4-user-manual/>`_

For this workshop the TurtleBot4 is used in a standard configuration.

Connection to the Robot
=======================

To conencto the TurtleBot4 robot, you can use SSH to access the robot's Raspberry PI.

.. code-block:: bash

    ssh ubuntu@<robot_ip_address>

The default password for the ``ubuntu`` user is ``turtlebot4``.

ROS Distro and Middleware
=========================

On the Robot we are using ROS2 Jazzy with FastRTPS as middleware.

Each Robot is using its own ROS2 Domain ID to avoid interference between the robots.
Please refer to the number on the TurtleBot4 to determine the correct Domain ID to use.

.. list-table:: ROS Distro and Middleware
	 :header-rows: 1

	 * - ROS Distro
	   - Middleware
	 * - Jazzy
	   - FastRTPS (rmw_fastrtps_cpp)

To try to connect to the robots from your PC please make sure to set the same Domain ID in your ROS2 environment.

.. code-block:: bash

    export ROS_DOMAIN_ID=<domain_id>

    export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

	export ROS_DISCOVERY_SERVER=<robot_ip_address>:11811
