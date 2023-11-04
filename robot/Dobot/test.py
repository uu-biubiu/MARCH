# from enum import Enum
from __future__ import annotations
from abc import ABC, abstractmethod

import serial
import serial.tools.list_ports

import DobotM1.DobotDllType as dType
import Logger
from Pressure import PressureImpl
from DobotM1.DobotDllType import PTPMode
# import Wrapper
import time
import math

api = dType.load()
logger = Logger.Logger
mfcs_clamp = PressureImpl(6)  # 控制夹爪的流控仪


# logger.instance().log("Start print logger msg!")

# class Wrapper:
#    def __init__(self):
#        pass


class Robot(ABC):
    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def setVelocity(self, VelocityRatio, AccelerationRatio):
        pass

    def MoveToPoint(self, X_position, Y_position, Z_position, R_angle):
        pass

    def SetRobotWait(self, RobotWaitTime):
        pass

    def Grab(self):
        pass

    def Release(self):
        pass

    def StartExec(self):
        pass

    def getVelocity(self) -> float:
        pass

    def getPosition(self) -> float:
        pass

    def stop(self):
        pass

    def reset(self):
        pass

    def get_alarm(self):
        pass

    def clear_alarm(self):
        pass


class RobotImpl(Robot):
    def __init__(self):
        super().__init__()
        self._implType = 1
        self._velocityratio = 2.0
        self._position = [0, 0, 0, 0]

    def connect(self):
        print("Connected to robot...")
        CON_STR = {
            dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
            dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
            dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
        # deviceList = dType.SearchDobot(api)

        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print("没有发现端口!")
            logger.instance().log("没有发现Dobot的端口!")  # 输出到logger中
        else:
            # plist_0 = list(plist[0])
            # serialName = plist_0[0]  # 先自动检测串口， 检测到可用串口，取出串口名
            # state = dType.ConnectDobot(api, serialName, 115200)[0]
            state = dType.ConnectDobot(api, "com3", 115200)[0]
            # print("可用端口名为>>>", serialName)
            # print("Connect status:", CON_STR[state])
            logger.instance().log("Dobot Connected!")  # 输出到logger中
        # ser = serial.Serial("COM6", 115200, timeout=30)
        # ser = serial.Serial(serialName, 115200, timeout=30)  # timeout=30 30s
        # print("可用端口名为>>>", ser.name)
        # ser.close()
        '''
        for index, devicePort in enumerate(deviceList):
            print(index, devicePort)
        enteredStr = input("Please enter your target M1 port by index: ")
        while not enteredStr.isnumeric() or int(enteredStr) >= len(deviceList) or int(enteredStr) < 0:
            enteredStr = input("The entered command is invalid. Please enter a valid index: ")
        print("Connecting ", deviceList[int(enteredStr)])
        state = dType.ConnectDobot(api, deviceList[int(enteredStr)], 115200)[0]
        print("Connect status:", CON_STR[state])
        '''
        if (state == dType.DobotConnect.DobotConnect_NoError):
            dType.SetQueuedCmdStopExec(api)
            dType.SetQueuedCmdClear(api)

    def disconnect(self):
        dType.SetQueuedCmdStopExec(api)
        dType.DisconnectDobot(api)
        # print("Dobot Disconnected.")
        logger.instance().log("Dobot DisConnected!")  # 输出到logger中

    def setVelocity(self, VelocityRatio, AccelerationRatio):
        print("setVelocity")
        dType.SetPTPCommonParams(api, VelocityRatio, AccelerationRatio, isQueued=1)
        loggerMsg = "Dobot setVelocity! VelocityRatio:{} AccelerationRatio{}".format(VelocityRatio, AccelerationRatio)
        logger.instance().log(loggerMsg)  # 输出到logger中
        # dType.SetQueuedCmdStartExec(api)

    def MoveToPoint(self, X_position, Y_position, Z_position, R_angle):
        print("moveToPoint")
        # RobotImpl().setVelocity(10, 10)
        # RobotImpl().SetRobotWait(1)
        dType.SetPTPCmd(api, PTPMode.PTPMOVJXYZMode, X_position, Y_position, Z_position, R_angle, isQueued=1)
        loggerMsg = "Dobot Moving! Position:[{},{},{},{}]".format(X_position, Y_position, Z_position, R_angle)
        logger.instance().log(loggerMsg)  # 输出到logger中
        # logger.instance().log("Dobot Moving!")  # 输出到logger中
        dType.SetQueuedCmdStartExec(api)

    def SetRobotWait(self, RobotWaitTime):
        print("setRobotWait")
        dType.SetWAITCmd(api, RobotWaitTime, isQueued=1)
        loggerMsg = "Dobot setRobotWait! WaitTime:{}秒".format(RobotWaitTime)
        logger.instance().log(loggerMsg)  # 输出到logger中
        dType.SetQueuedCmdStartExec(api)

    def Grab(self):
        mfcs_clamp.connect()
        mfcs_clamp.setPressure(1, 9)  # 设置正压
        time.sleep(1)
        mfcs_clamp.purgeOn(1)  # 关闭爪
        # logger.instance().log("Dobot Grabbing!")  # 输出到logger中
        print('Grabbing...')

    def Release(self):
        mfcs_clamp.purgeOff(1)
        time.sleep(1)
        mfcs_clamp.setPressure(1, -9)  # 设置负压
        time.sleep(1)
        mfcs_clamp.purgeOn(1)  # 打开爪
        time.sleep(1)
        mfcs_clamp.purgeOff(1)
        mfcs_clamp.disconnect()
        # logger.instance().log("Dobot softRelease!")  # 输出到logger中
        print('Releasing...')

    def StartExec(self):
        lastQueuedIndex = dType.SetWAITCmd(api, 0.1, isQueued=1)[0]
        dType.SetQueuedCmdStartExec(api)
        # Wait for Executing Last Command
        while lastQueuedIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
            dType.dSleep(10)
        dType.SetQueuedCmdClear(api)

    def getVelocity(self) -> float:
        print("Get robot velocity ratio...")
        getParams = dType.GetPTPCommonParams(api)
        self._velocityratio = getParams[0]
        logger.instance().log("Get dobot velocity ratio...")  # 输出到logger中
        return self._velocityratio

    def getPosition(self) -> float:
        print("Get robot position...")
        pos = dType.GetPose(api)
        self._position = [pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7]]
        # time.sleep(0.5)
        logger.instance().log("Get dobot position...")  # 输出到logger中
        return self._position

    def stop(self):
        print("stop")
        dType.SetQueuedCmdForceStopExec(api)
        logger.instance().log("Dobot stop!")  # 输出到logger中

    def reset(self):
        dType.SetQueuedCmdClear(api)
        logger.instance().log("Dobot reset!")  # 输出到logger中

    def get_alarm(self):
        dType.GetAlarmsState(api, 1000)   #return [alarmsState.raw, len.value]

    def clear_alarm(self):
        dType.ClearAllAlarmsState(api)


def test_code() -> None:
    #测试get_alarm
    dobot_m1 = RobotImpl()
    dobot_m1.connect()

    alarm = []
    alarm = dobot_m1.get_alarm()
    print(alarm)
    time.sleep(5)

    dobot_m1.disconnect()


if __name__ == "__main__":
    test_code()
