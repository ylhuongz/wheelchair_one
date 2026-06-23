**Setup Command**
cd ~/wheelchair_ws
colcon build --symlink-install
source install/setup.bash

Terminal 1:
ros2 launch wheelchair_one rsp.launch.py

Terminal 2:
rviz2

Terminal 3:
ros2 run joint_state_publisher_gui joint_state_publisher_gui
