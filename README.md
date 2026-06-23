**NOTE:** This is for ROS2 Jazzy

---
# Setup Commands
## First-time setup
```bash
sudo apt update
sudo apt upgrade
sudo apt install ros-jazzy-desktop    # install ROS2 Jazzy
source /opt/ros/jazzy/setup.bash    # connect terminal to ros2
sudo apt-get install ros-jazzy-ros-gz    # install gazebo
sudo apt install ros-jazzy-joint-state-publisher-gui    # install sliders for wheels
```
## After first-time setup
```bash
cd ~/wheelchair_ws
colcon build --symlink-install    # first-time running package ONLY
source install/setup.bash
ros2 launch wheelchair_one rsp.launch.py
```
Once RVIZ is up and running, do the following to see the robot model:
```bash
click "Add" --> "TF"
click "Add" --> "RobotModel"
```
