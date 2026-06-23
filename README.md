**Setup Command**

cd ~/wheelchair_ws

colcon build --symlink-install  # first-time running package ONLY

source install/setup.bash

ros2 launch wheelchair_one rsp.launch.py


**Once RVIZ is up and running, do the following to see the robot model:**

click "Add" --> "TF"

click "Add" --> "RobotModel"
