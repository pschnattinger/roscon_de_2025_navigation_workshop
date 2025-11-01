================
TurtleBot4 Setup
================

General
=======

The TurtleBot4 is a popular mobile robot platform designed for education and research in robotics.
It is equipped with various sensors and actuators, making it suitable for a wide range of applications, including navigation, mapping, and manipulation.

The TurtleBot4 documentation can be found here: `TurtleBot4 Documentation <https://turtlebot.github.io/turtlebot4-user-manual/>`_

For this workshop the TurtleBot4 is used in a standard configuration.

ROS Distro and Middleware
#########################

On the Robot we are using ROS2 Jazzy with CycloneDDS as middleware.

Each Robot is using its own ROS2 Domain ID to avoid interference between the robots.
Please refer to the number on the TurtleBot4 to determine the correct Domain ID to use.

.. list-table:: ROS Distro and Middleware
	 :header-rows: 1

	 * - ROS Distro
	   - Middleware
	 * - Jazzy
	   - CycloneDDS (rmw_cyclonedds_cpp)

To try to connect to the robots from your PC please make sure to set the same Domain ID in your ROS2 environment.

.. code-block:: bash

    export ROS_DOMAIN_ID=<domain_id>

    export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

    export CYCLONEDDS_URI=/path/to/your/cyclonedds.xml

As cyclonedds.xml you can use the following template and adjust the settings as needed:

.. code-block:: xml
   :linenos:

   <CycloneDDS xmlns="https://cdds.io/config">
     <Domain>
       <General>
         <Interfaces>
           <!-- Adjust to your network interface -->
           <NetworkInterface name="wlp3s0" priority="default" multicast="default"/>
         </Interfaces>
         <DontRoute>true</DontRoute>
       </General>
     </Domain>
   </CycloneDDS>
Simulation
==========
