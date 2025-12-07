### 📋 项目路线图 (Roadmap)

本项目旨在基于 ROS 2 和 MoveIt 2 构建一套具备视觉感知能力的机械臂控制系统，并充分利用 GPU 加速以实现高性能规划。

#### 🚀 第一阶段：基础控制 (Basic Control)
**目标：** 完成机械臂的运动学配置，实现仿真环境中的运动规划。
- [x] **MoveIt 配置生成**：使用 `MoveIt Setup Assistant` 生成配置包 (`arm_robot_moveit_config`)。
    - [x] 生成碰撞矩阵 (Self-Collision Matrix)。
    - [x] 定义虚拟关节 (`virtual_joint` -> `world`)。
    - [x] 配置规划组 (`planning_group`: `arm`)。
    - [x] 配置控制器 (`FollowJointTrajectory`)。
- [x] **功能验证**：
    - [x] 编译并在 RViz 中运行 `demo.launch.py`。
    - [x] 测试拖拽交互标记进行简单的路径规划与执行。

相关笔记：[MoveIt2 基础配置与使用记录](doc/moveit2.md)

#### 👁️ 第二阶段：视觉感知集成 (Vision Integration)
**目标：** 接入 Intel Realsense D435，实现环境感知与避障。
- [ ] **硬件驱动**：集成 `realsense-ros`，确保在 ROS 2 中获取点云数据。
- [ ] **手眼标定 (Hand-Eye Calibration)**：
    - [ ] 使用 `moveit_calibration_gui` 进行标定 (Eye-in-Hand 或 Eye-to-Hand)。
    - [ ] 获取并保存相机与机械臂基座的 TF 变换矩阵。
- [ ] **环境避障**：
    - [ ] 配置 MoveIt 的 `sensors_3d.yaml` (Octomap)。
    - [ ] 验证机械臂在规划路径时自动避开相机视野内的障碍物。

#### ⚡ 第三阶段：GPU 加速与进阶 (GPU Acceleration & Advanced)
**目标：** 利用 RTX 3090 提升规划速度与仿真真实度。
- [ ] **高性能仿真**：
    - [ ] 从 Gazebo 迁移至 **NVIDIA Isaac Sim**。
    - [ ] 在 Isaac Sim 中导入 URDF 并配置物理属性。
- [ ] **感知加速**：
    - [ ] 使用 **Isaac ROS** 替换 CPU 版的图像处理节点。
    - [ ] (可选) 部署 **GraspNet** 等深度学习模型进行 6-DoF 抓取姿态推理。
- [ ] **极速规划 (可选)**：
    - [ ] 探索接入 **NVIDIA cuRobo (cuMotion)** 替代 OMPL，实现毫秒级动态规划。



### 一些记录

solidworks导出urdf并在ros2中使用的[demo记录](doc/sw-urdf-ros2-demo.md)

