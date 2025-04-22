#常用指令
#归位
rosservice call /DobotServer/SetPTPCmd "{ptpMode: 0, x: 230, y: 37, z: 9, r: -96}"
#X:215, Y:0, Z::25, R:0 ，这个是能转到车头的坐标，r代表的是舵机转的角度


#气泵吸取suck：1吸取，0释放
rosservice call /DobotServer/SetEndEffectorSuctionCup "enableCtrl: 1
suck: 0
isQueued: 0"

#获取当前坐标
rosservice call /DobotServer/GetPose

#归零
rosservice call /DobotServer/SetHOMECmd “{}”

#列出当前可使用的串口
ls /dev/tty*
#调用机械臂时，串口无效
vim /home/eaibot/moveit_ws/src/moveit/dobot/launch/DobotServer.launch
#找到 <param name="DobotServer/dobot_serial" value="/dev/ttyUSB2" /> 这一行，将 value 属性的值修改为正确的端口名
<param name="DobotServer/dobot_serial" value="/dev/ttyUSB0" />#将ttyUSB0更改为自己的实际串口

