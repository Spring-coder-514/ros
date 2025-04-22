#所有常见指令

#!/bin/bash

# 定义清理函数
cleanup() {
    echo "Stopping ROS nodes..."
    # 杀死所有由脚本启动的 ROS 进程
    kill $LAUNCH_PID 2>/dev/null
    kill $LAUNCH_PID_DOBOT 2>/dev/null
    exit 1
}

# 捕获 Ctrl+C (SIGINT) 信号，并调用清理函数
trap cleanup SIGINT

# 进入第一个工作空间并启动 ROS 启动文件

source /home/eaibot/dashgo_ws/devel/setup.sh

roslaunch dashgo_nav navigation_imu_2.launch &
LAUNCH_PID=$!
echo "Started dashgo_nav navigation_imu_2.launch with PID $LAUNCH_PID"

# 等待 5 秒钟，确保第一个节点启动完毕
sleep 5

# 进入第二个工作空间并启动第二个 ROS 启动文件

source /home/eaibot/moveit_ws/devel/setup.sh

roslaunch dobot DobotServer.launch &
LAUNCH_PID_DOBOT=$!
echo "Started dobot DobotServer.launch with PID $LAUNCH_PID_DOBOT"

# 等待 3 秒钟，确保第二个节点启动完毕
sleep 3
#roslaunch usb_cam usb_cam-test.launch &LAUNCH_PID_DOBOT=$!
roslaunch map_server map_server.launch map_file:=/home/eaibot/dashgo_ws/src/dashgo/dashgo_nav/maps/87_13.yaml &LAUNCH_PID_DOBOT=$!

echo "配置加载完毕"
sleep 2
rosservice call /DobotServer/SetHOMECmd
sleep 60
echo "执行导航"
python /home/eaibot/final3.py

echo "执行夹取"
#python /home/eaibot/arm.py
# 等待用户输入，保持脚本运行i
#roslaunch usb_cam usb_cam-test.launch 
#roslaunch map_server map_server.launch map_file:=/home/eaibot/dashgo_ws/src/dashgo/dashgo_nav/maps/87_13.yaml &LAUNCH_PID_DOBOT=$!

wait
