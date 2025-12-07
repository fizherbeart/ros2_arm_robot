

修改CmakeLists.txt 和 package.xml，换成ament_cmake

package.xml
```
-  <buildtool_depend>catkin</buildtool_depend>
-  <depend>roslaunch</depend>
-  <depend>robot_state_publisher</depend>
-  <depend>rviz</depend>
-  <depend>joint_state_publisher_gui</depend>
-  <depend>gazebo</depend>
+  <buildtool_depend>ament_cmake</buildtool_depend>^M
+  <exec_depend>robot_state_publisher</exec_depend>^M
+  <exec_depend>rviz2</exec_depend>^M
+  <exec_depend>joint_state_publisher_gui</exec_depend>^M
+  <exec_depend>gazebo</exec_depend>^M
   <export>
-    <architecture_independent />
+   <build_type>ament_cmake</build_type>^M
   </export>
 </package>
```

CMakeLists.txt
```
cmake_minimum_required(VERSION 3.5)
project(arm_robot)
find_package(ament_cmake REQUIRED)
foreach(dir config launch meshes urdf rviz)
  install(DIRECTORY ${dir}/
    DESTINATION share/${PROJECT_NAME}/${dir})
endforeach()
ament_package()
```


```bash
conda deactivate # 确保不在conda环境下
```

安装依赖
```bash
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

编译
```bash
colcon build --symlink-install --packages-select arm_robot
```

用ai根据display.launch生成新的launch文件display.launch.py


运行
```bash
ros2 launch arm_robot display.launch.py
```

在rviz中选择base_link作为Fixed Frame
添加RobotModel显示机器人模型，topic选择/robot_description
添加TF显示坐标系
保存rviz配置文件为arm_robot.rviz，放在rviz文件夹下


修改CMakeLists.txt, `foreach(dir config launch meshes urdf rviz)` 添加rviz， 重新编译
```bash
rm -rf build/ install/ log/
colcon build --symlink-install --packages-select arm_robot
``` 
