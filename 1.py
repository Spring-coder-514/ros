#常用指令
#归位
rosservice call /DobotServer/SetPTPCmd "{ptpMode: 0, x: 230, y: -25, z: 15, r: -96}"
#X:215, Y:0, Z::25, R:0 ，这个是能转到车头的坐标


#气泵吸取suck：1吸取，0释放
rosservice call /DobotServer/SetEndEffectorSuctionCup "enableCtrl: 1
suck: 0
isQueued: 0"

#获取当前坐标
rosservice call /DobotServer/GetPose

#归零
rosservice call /DobotServer/SetHOMECmd

#列出当前可使用的串口
ls /dev/tty*


