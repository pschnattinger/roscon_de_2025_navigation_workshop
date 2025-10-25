======================================
Lichtblick Suite Connection with Robot
======================================

This section describes how to install **Lichtblick Suite** on your PC and how to connect it to a running **ROS system** using the **rosbridge_websocket** interface.

.. contents::
   :local:
   :depth: 2


Overview
========

The **Lichtblick Suite** is a browser-based visualization and interaction tool for robots running ROS 2.
This can be used as an alternative to RViz for visualizing sensor data, robot state, and other information.
It communicates through a **WebSocket connection** provided by the ``rosbridge_server`` package.

By the end of this guide, you will have:

- Installed the Lichtblick Suite desktop application
- Started a ``rosbridge_websocket`` server
- Connected Lichtblick to your ROS system

Installation
============

Download the Lichtblick Suite
-----------------------------

   Lichtblick Suite can be found in the following GitHub repository:

   `Lichtblick Suite Repository <https://github.com/lichtblick-suite/lichtblick>`_

   You can either download the latest release from the `releases page <https://github.com/Lichtblick-Suite/lichtblick/releases>`_ or clone the repository directly.

Connect to Robot
================

   To connect Lichtblick to your robot's ROS system, follow these steps:

   1. Connect to the robot via ssh:

      .. code-block:: bash

         ssh ubuntu@<robot_ip_address>

   2. Ensure that the ``rosbridge_websocket`` server is running on your robot. You can start it with the following command:

      .. code-block:: bash

         ros2 launch rosbridge_server rosbridge_websocket_launch.xml

   3. Open the Lichtblick Suite application on your PC.

   4. In Lichtblick, navigate to the connection settings and enter the IP address and port of the robot running the ``rosbridge_websocket`` server (default port is 9090).

      .. image:: ../assets/lichtblick/lichtblick_connection.png
         :alt: Lichtblick Connection Settings
         :align: center


   5. Click "Open" to establish the connection.

   Once connected, you should be able to visualize and interact with your robot's ROS system through the Lichtblick Suite interface.
