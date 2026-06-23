### NOTE: ### This is for ROS2 Jazzy

# Setup Command
**first time setup**

sudo apt update

sudo apt upgrade

sudo apt install ros-jazzy-desktop  *# install ros2 jazzy*

source /opt/ros/jazzy/setup.bash  *# connect terminal to ros2*

sudo apt-get install ros-jazzy-ros-gz  *# install gazebo*

sudo apt install ros-jazzy-joint-state-publisher-gui  *# install sliders for wheels*

**after first time**

cd ~/wheelchair_ws

colcon build --symlink-install  *# first-time running package ONLY*

source install/setup.bash

ros2 launch wheelchair_one rsp.launch.py


**Once RVIZ is up and running, do the following to see the robot model:**

click "Add" --> "TF"

click "Add" --> "RobotModel"
