=======================
Nav2 on the TurtleBot4
=======================


In this section, we will cover the steps required to perform navigation using the TurtleBot4 robot platform.

General Setup
=============

The Turtlebot4 runs with a Raspberry Pi 4 as main computer. This is quiet small when it comes to power and performance.

In case you encounter slow startup times for nodes or docker containers please be patient and wait a bit longer.

To start navigation on the turtlebot please go into the roscon_de_2025_navigation_workshop/turtlebot4_navigation/ folder and start the navigation stack with: folder and run.

.. code-block:: bash

   docker compose up -d

This should start two containers, one for the localization and one for the navigation stack.

.. code-block:: bash

   docker ps

You should see something like this:

.. code-block:: bash

    CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS     NAMES
    acba7465b33a   turtlebot4_navigation:kilted   "/entrypoint.sh bash…"   42 minutes ago   Up 13 minutes             ros2-turtlebot4-navigation-kilted
    c4f03943659e   turtlebot4_navigation:kilted   "/entrypoint.sh bash…"   42 minutes ago   Up 42 minutes             ros2-turtlebot4-localization-kilted


Initialize and send a goal with Lichtblick
==========================================

Now the navigation is started try to localize the robot over Lichtblick

Use the publish tool to send an initial pose to the robot.

Make sure to select the initialpose topic in the publish section.


.. image:: ../assets/lichtblick/init_pose.gif
         :alt: Lichtblick Localize Robot
         :align: center


With the robot localized now you should be able to send and monitor goals over lichtblick as well.
