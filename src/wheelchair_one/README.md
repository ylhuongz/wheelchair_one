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
```
### Launch Rviz
```bash
ros2 launch wheelchair_one rsp.launch.py
```

### Launch Gazebo
Note: Make sure all terminals are sourced

Terminal 1 (launch):
```bash
ros2 launch wheelchair_one gazebo_model.launch.py
```
Terminal 2 (lidar readings):
```bash
ros2 topic echo /scan --field ranges
```
Terminal 3 (control):
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
