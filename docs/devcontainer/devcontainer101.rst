Devcontainer 101
=================

Purpose
-------
This document explains how to open the project in a dev container using
Visual Studio Code on Ubuntu.
The project already includes a `.devcontainer` folder with the required config under roscon_de_2025_navigation_workshop/dev_container.

Prerequisites
-------------
- Docker installed and running on Ubuntu::

      sudo apt update
      sudo apt install docker.io
      sudo usermod -aG docker $USER   # log out and back in after this

- Visual Studio Code installed.
- VS Code extension **Dev Containers** installed.
- Inside the devcontainer.json, change the value of the <ip-address> placeholder in the ``ROS_DISCOVERY_SERVER`` environment variable to the IP address and <domain-id> placeholder to the ``ROS_DOMAIN_ID`` of the TurtleBot4 you want to connect to.

Starting the Dev Container
--------------------------
Follow one of the two methods below.

Method A: Using the VS Code Popup (Click-Based)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Open the project folder in VS Code:
   - **File → Open Folder…**
   - Select the folder that contains `.devcontainer/`.

2. VS Code will detect the dev container configuration and show a popup
   in the bottom-right corner saying:
   **“Folder contains a Dev Container configuration”**.

3. Click the button:
   **“Reopen in Container”**.

4. VS Code will build the container and reopen the window inside it.

5. Open a terminal:
   - **Terminal → New Terminal**
   The terminal now runs **inside** the dev container.

You can choose not to use vscode terminal. You can run the following command in your local terminal to exec into the devcontainer:
.. code-block:: bash

   docker exec -it kilted_dev_container bash

Method B: Using the Command Palette
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Open the project folder in VS Code.

2. Press `Ctrl+Shift+P` to open the Command Palette.

3. Run:
   ``Dev Containers: Reopen in Container``

4. After the rebuild/open process completes, open a terminal:
   - **Terminal → New Terminal**

You are now ready to work inside the dev container.
