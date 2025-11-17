==========================
Mapping on the TurtleBot4
==========================

In this section, we will cover the steps required to perform mapping using the TurtleBot4 robot platform.

The goal is to generate a 2D occupancy grid map of the environment using the robot's onboard rplidar.

For that we want to run mapping in combination with lichtblick for visualization and a joystick or the keyboard teleoperation for controlling the robot.

First make sure you can see ros topics from the robot on your PC.
Please refer to the :doc:`TurtleBot4 Setup </turtlebot4/turtlebot4>` section for details on how to connect to the robot and set the correct ROS_DOMAIN_ID

Launch Mapping on the Robot
===========================

Go to the robot via ssh like shown in the :doc:`TurtleBot4 Setup </turtlebot4/turtlebot4>` section.

Best way to keep the slam running by using tmux or screen.

.. code-block:: bash

    ssh ubuntu@<robot_ip_address>
    tmux new
    ros2 launch turtlebot4_navigation slam.launch.py

On your devcontainer / PC start teleop keyboad to control the robot.

.. code-block:: bash

    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true

Important here is to actually run it with stamped:=true because with latest changes in ROS2 the hardware topics expect a `geometry_msgs/TwistStamped` message.

Now move the robot around to map the environment.

.. image:: ../assets/mapping/initial_map.gif
   :alt: Mapping with TurtleBot4
   :width: 800px

To save the map one can use the map_saver node from map_server package.

.. code-block:: bash

    ros2 run nav2_map_server map_saver_cli -f "map_name" --ros-args -p map_subscribe_transient_local:=true

This will save two files `map_name.yaml` and `map_name.pgm` in the current directory.

Afer generating the map on the robot one needs to move the files into the envs folder within the roscon folder under

.. code-block:: bash

    /home/ubuntu/roscon_de_2025_navigation_workshop/envs/

This map will be used to navigate the robot in the next section.

Once you have done this you need to set the environment variable on the .env file located under ``/home/ubuntu/roscon_de_2025_navigation_workshop/.env`` on the robot.

Change the map path to the localation of the ``.yaml`` in the ``turtlebot4_navigation/envs/`` folder.

.. code-block:: bash

    ROS_DOMAIN_ID=4
    MAP_PATH=node/node.yaml


.. note::

   Make sure to stop the mapping node on the robot by pressing ``CTRL+C`` in the tmux/screen session where the mapping was started.


Starting localization
=====================

The turtlebot4 uses AMCL for localization. To make the turtlebot use your newly created map you need to start the localization stack with the following command on the robot:

.. code-block:: bash

   cd /home/ubuntu/roscon_de_2025_navigation_workshop/turtlebot4_navigation/
   docker compose -f docker-compose.yaml up -d turtlebot-localization

Verify that the localization is running.

.. code-block:: bash

   docker logs -f ros2-turtlebot4-localization-kilted

You should see something like this:

.. code-block:: bash

    [INFO] [launch]: All log files can be found below /root/.ros/log/2025-07-11-22-05-58-298103-turtlebot4-1
    [INFO] [launch]: Default logging verbosity is set to INFO
    [INFO] [map_server-1]: process started with pid [17]
    [INFO] [amcl-2]: process started with pid [18]
    [INFO] [lifecycle_manager-3]: process started with pid [19]
    [amcl-2] [INFO] [1752271559.690757785] [amcl]:
    [amcl-2] 	amcl lifecycle node launched.
    [amcl-2] 	Waiting on external lifecycle transitions to activate
    [amcl-2] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
    [amcl-2] [INFO] [1752271559.696228689] [amcl]: Creating
    [lifecycle_manager-3] [INFO] [1752271559.752670179] [lifecycle_manager_localization]: Creating
    [lifecycle_manager-3] [INFO] [1752271559.754069410] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
    [map_server-1] [INFO] [1752271559.898383307] [map_server]:
    [map_server-1] 	map_server lifecycle node launched.
    [map_server-1] 	Waiting on external lifecycle transitions to activate
    [map_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
    [map_server-1] [INFO] [1752271559.898920766] [map_server]: Creating
    [lifecycle_manager-3] [INFO] [1752271561.775447129] [lifecycle_manager_localization]: Waiting for service map_server/get_state...
    [lifecycle_manager-3] [INFO] [1752271562.386863928] [lifecycle_manager_localization]: Creating and initializing lifecycle service servers
    [lifecycle_manager-3] [INFO] [1752271562.514664577] [lifecycle_manager_localization]: Starting managed nodes bringup...
    [lifecycle_manager-3] [INFO] [1752271562.514846371] [lifecycle_manager_localization]: Configuring map_server
    [map_server-1] [INFO] [1752271562.520246313] [map_server]: Configuring
    [map_server-1] [INFO] [1752271562.520537478] [map_io]: Loading yaml file: /envs/node/node.yaml
    [map_server-1] [INFO] [1752271562.522173169] [map_io]: resolution: 0.05
    [map_server-1] [INFO] [1752271562.522250280] [map_io]: origin[0]: -7.99
    [map_server-1] [INFO] [1752271562.523021996] [map_io]: origin[1]: -0.693
    [map_server-1] [INFO] [1752271562.523062589] [map_io]: origin[2]: 0
    [map_server-1] [INFO] [1752271562.523149532] [map_io]: free_thresh: 0.25
    [map_server-1] [INFO] [1752271562.523174810] [map_io]: occupied_thresh: 0.65
    [map_server-1] [INFO] [1752271562.523208699] [map_io]: mode: trinary
    [map_server-1] [INFO] [1752271562.523233458] [map_io]: negate: 0
    [map_server-1] [INFO] [1752271562.526091585] [map_io]: Loading image_file: /envs/node/node.pgm
    [map_server-1] [INFO] [1752271562.533684214] [map_io]: Read map /envs/node/node.pgm: 223 X 136 map @ 0.05 m/cell
    [lifecycle_manager-3] [INFO] [1752271562.641110902] [lifecycle_manager_localization]: Configuring amcl
    [amcl-2] [INFO] [1752271562.641935766] [amcl]: Configuring
    [amcl-2] [INFO] [1752271562.642250931] [amcl]: initTransforms
    [amcl-2] [INFO] [1752271562.724133400] [amcl]: initPubSub
    [amcl-2] [INFO] [1752271562.785693075] [amcl]: Subscribed to map topic.
    [lifecycle_manager-3] [INFO] [1752271562.834282420] [lifecycle_manager_localization]: Activating map_server
    [map_server-1] [INFO] [1752271562.834894008] [map_server]: Activating
    [map_server-1] [INFO] [1752271562.836224294] [map_server]: Creating bond (map_server) to lifecycle manager.
    [amcl-2] [INFO] [1752271562.838066447] [amcl]: Received a 223 X 136 map @ 0.050 m/pix
    [lifecycle_manager-3] [INFO] [1752271562.972523899] [lifecycle_manager_localization]: Server map_server connected with bond.
    [lifecycle_manager-3] [INFO] [1752271562.972698342] [lifecycle_manager_localization]: Activating amcl
    [amcl-2] [INFO] [1752271562.974320034] [amcl]: Activating
    [amcl-2] [INFO] [1752271562.974475421] [amcl]: Creating bond (amcl) to lifecycle manager.
    [lifecycle_manager-3] [INFO] [1752271563.099515424] [lifecycle_manager_localization]: Server amcl connected with bond.
    [lifecycle_manager-3] [INFO] [1752271563.099711996] [lifecycle_manager_localization]: Managed nodes are active
    [lifecycle_manager-3] [INFO] [1752271563.099771126] [lifecycle_manager_localization]: Creating bond timer...
    [amcl-2] [INFO] [1752271563.111980535] [amcl]: createLaserObject
    [amcl-2] [WARN] [1752271564.707614195] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271566.727678757] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271568.810418486] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271570.812753530] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271572.967777096] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271575.061922796] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...
    [amcl-2] [WARN] [1752271577.209159307] [amcl]: AMCL cannot publish a pose or update the transform. Please set the initial pose...


Now follow the descriptions in the :doc:`Lichtblick Setup </lichtblick/lichtblick>` section to connect Lichtblick to your robot and send an initial pose to localize the robot on the map and move it around with teleop.

.. code-block:: bash

   ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true
