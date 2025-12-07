import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_name = 'arm_robot'
    pkg_path = get_package_share_directory(pkg_name)
    
    # 获取 URDF 文件路径
    urdf_file = os.path.join(pkg_path,'urdf','arm_robot.urdf')
    
    # 获取 Rviz 配置文件路径
    rviz_config_file = os.path.join(pkg_path,'rviz','arm_robot.rviz')

    # 读取 URDF 内容
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # 设置 Rviz 配置文件路径 (如果有的话)
    # 注意：原本的 launch 文件引用了 (find arm_robot)/urdf.rviz
    # 请确保该文件已被 CMakeLists.txt 安装，或者手动指定一个默认路径
    # 这里我们暂时不强制加载特定 rviz 配置，以免再次报错
    
    return LaunchDescription([
        # 节点 1: robot_state_publisher
        # 负责发布机器人的 TF 树和 robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),

        # 节点 2: joint_state_publisher_gui
        # 提供一个 GUI 滑块来控制关节角度
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # 节点 3: rviz2
        # 可视化工具
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            # 如果你有保存好的 .rviz 配置，取消下面这行的注释并填入正确路径
            arguments=['-d', rviz_config_file]
        ),
    ])