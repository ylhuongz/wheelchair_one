# Differential Drive ROS2 and Gazebo Launch File

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # Name has to match robot name in Xacro file
    robotXacroName = 'wheelchair'

    # Name of package and folder used to define the paths
    namePackage = 'wheelchair_one'

    # Relative path to robot_core.xacro
    modelFileRelativePath = 'description/robot.urdf.xacro'

    # Uncomment for your own empty world model
    # must create empty_world.world
    # relative path to Gazebo world file
    worldFileRelativePath = 'worlds/obstacles.sdf'

    # Absolute path to model
    pathModelFile = os.path.join(get_package_share_directory(namePackage), modelFileRelativePath)

    # Uncomment for your own world model
    # absolute path to world model
    pathWorldFile = os.path.join(get_package_share_directory(namePackage), worldFileRelativePath)

    # Get robot description from xacro model file
    robotDescription = xacro.process_file(pathModelFile).toxml()

    # Launch file from gazebo_ros package
    gazeboRosPackageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('ros_gz_sim'),
                                                                                                     'launch', 'gz_sim.launch.py'))

    # Launch Description
    # world = LaunchConfiguration('world')
    # loadWorld = DeclareLaunchArgument('world', default_value='empty.sdf', description='World file to load')

    # For using your own world model
    gazeboLaunch = IncludeLaunchDescription(gazeboRosPackageLaunch, launch_arguments={'gz_args': f'-r -v 4 "{pathWorldFile}"', 'on_exit_shutdown': 'true'}.items())

    # For using an empty world model
    # gazeboLaunch = IncludeLaunchDescription(gazeboRosPackageLaunch, launch_arguments={'gz_args': ['-r -v 4 empty.sdf'], 'on_exit_shutdown': 'true'}.items())

    # Gazebo Node
    spawnModelNodeGazebo = Node(
        package = 'ros_gz_sim',
        executable = 'create',
        arguments = ['-name', 'wheelchair',
                     '-topic', 'robot_description'],
        output = 'screen',
    )

    # Robot State Publisher Node
    nodeRobotStatePublisher = Node(
        package = 'robot_state_publisher',
        executable = 'robot_state_publisher',
        output = 'screen',
        parameters = [{'robot_description': robotDescription,
                       'use_sim_time': True}]
    )

    # ROS2 Controls
    bridgeParams = os.path.join(get_package_share_directory(namePackage), 'config', 'bridge_parameters.yaml')

    startGazeboRosBridgeCmd = Node(
        package = 'ros_gz_bridge',
        executable = 'parameter_bridge',
        arguments = ['--ros-args', '-p',
                     f'config_file:={bridgeParams}'],
        output = 'screen'
    )

    rvizNode = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    # Add the nodes to launch
    return LaunchDescription([
        # loadWorld,
        gazeboLaunch,
        nodeRobotStatePublisher,
        startGazeboRosBridgeCmd,
        spawnModelNodeGazebo,
        rvizNode
    ])

    return launchDescriptionObject