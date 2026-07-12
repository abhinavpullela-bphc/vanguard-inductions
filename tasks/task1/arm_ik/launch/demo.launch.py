import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg = get_package_share_directory("arm_ik")
    with open(os.path.join(pkg, "urdf", "arm3dof.urdf")) as f:
        robot_description = f.read()

    return LaunchDescription([
        DeclareLaunchArgument("target_x", default_value="0.30"),
        DeclareLaunchArgument("target_y", default_value="0.15"),
        DeclareLaunchArgument("target_z", default_value="0.25"),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": robot_description}],
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", os.path.join(pkg, "rviz", "arm.rviz")],
        ),
        Node(
            package="arm_ik",
            executable="move_arm",
            parameters=[{
                "target_x": ParameterValue(LaunchConfiguration("target_x"), value_type=float),
                "target_y": ParameterValue(LaunchConfiguration("target_y"), value_type=float),
                "target_z": ParameterValue(LaunchConfiguration("target_z"), value_type=float),
            }],
        ),
    ])
