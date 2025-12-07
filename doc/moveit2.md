安装moveit2
```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-moveit 
sudo apt install ros-$ROS_DISTRO-moveit-setup-assistant
```

编译项目
```bash
rm -rf build/ install/ log/
colcon build --symlink-install --packages-select arm_robot
source install/setup.bash
```

进入可视化界面进行配置，生成代码放到`src/arm_robot_moveit_config`包中
```bash
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```


安装依赖并编译
安装之前需要注释package.xml里的 `<exec_depend>warehouse_ros_mongo</exec_depend>` 
简单来说：这个包是用来连接数据库存取数据的（比如存规划场景），对于你现在只想让机械臂动起来（Demo）来说，它完全不是必须的。ros-humble-warehouse-ros-mongo 这个包在 Ubuntu 22.04 (Humble) 的源里经常找不到或者名字变了，导致 rosdep 报错。
```bash
# 要梯子
sudo rosdep init  # 如果提示已存在，可以忽略
rosdep update
rosdep install --from-paths src --ignore-src -r -y
# 防止rosdep没装全
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-controller-manager
```

---

ROS 2 Humble 版本中常见问题
检查joint_limits.yaml，数字是否都有小数点，否则会报错

参数类型不匹配（导致 move\_group 崩溃）

这是最严重的问题，导致了 `move_group` 进程直接挂掉（Exit code -6）。

  * **报错日志：**
    `parameter 'robot_description_planning.joint_limits.joint_6.max_velocity' has invalid type: expected [double] got [integer]`
  * **原因：**
    ROS 2 Humble 对参数类型非常严格。MoveIt 生成的 `joint_limits.yaml` 文件里，某个关节的速度限制写成了整数（比如 `1`），但 ROS 2 强制要求它是浮点数（比如 `1.0`）。
  * **解决方法：**
    1.  打开你的 MoveIt 配置包中的关节限制文件。路径通常是：
        `src/arm_robot_moveit_config/config/joint_limits.yaml`
    2.  检查所有 `max_velocity` 和 `max_acceleration` 的值。
    3.  **把所有整数改成带小数点的形式**。
          * **错误示例：** `max_velocity: 1`
          * **正确示例：** `max_velocity: 1.0`
    4.  保存文件。

---

启动demo
```bash
colcon build --packages-select arm_robot_moveit_config
source install/setup.bash
ros2 launch arm_robot_moveit_config demo.launch.py
```


