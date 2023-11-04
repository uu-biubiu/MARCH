# from enum import Enum
from __future__ import annotations

import os
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


# precigenome_claw = PressureImpl()  # 控制夹爪的流控仪
# logger.instance().log("Start print logger msg!")


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

    def MoveToPoint_Joint(self, X_joint, Y_joint, Z_joint, R_angle):
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

    def start(self):
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

    def connect(self, PORT) -> int:
        dobot_connect_state = 0
        PORT = PORT.lower()
        print(PORT)
        print("Connected to robot...")
        state = dType.ConnectDobot(api, PORT, 115200)[0]
        if (state == dType.DobotConnect.DobotConnect_NoError):
            dType.SetQueuedCmdStopExec(api)
            dType.SetQueuedCmdClear(api)
            print("Dobot连接成功")
            dobot_connect_state = 1
            logger.instance().log("Dobot Connected!")  # 输出到logger中
        else:
            dobot_connect_state = 0
        print(dobot_connect_state)
        return dobot_connect_state

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

    # 笛卡尔坐标系下MOVEJ方式移动
    def MoveToPoint(self, X_position, Y_position, Z_position, R_angle):
        print("moveToPoint")
        # RobotImpl().setVelocity(10, 10)
        # RobotImpl().SetRobotWait(1)
        dType.SetPTPCmd(api, PTPMode.PTPMOVJXYZMode, X_position, Y_position, Z_position, R_angle, isQueued=1)
        loggerMsg = "Dobot Moving! Position:[{},{},{},{}]".format(X_position, Y_position, Z_position, R_angle)
        logger.instance().log(loggerMsg)  # 输出到logger中
        # logger.instance().log("Dobot Moving!")  # 输出到logger中
        dType.SetQueuedCmdStartExec(api)

    # 关节坐标系下MOVEJ方式移动
    def MoveToPoint_Joint(self, X_joint, Y_joint, Z_joint, R_angle):
        print("moveToPoint_joint")
        # RobotImpl().setVelocity(10, 10)
        # RobotImpl().SetRobotWait(1)
        dType.SetPTPCmd(api, PTPMode.PTPMOVJANGLEMode, X_joint, Y_joint, Z_joint, R_angle, isQueued=1)
        loggerMsg = "Dobot Moving! Position:[{},{},{},{}]".format(X_joint, Y_joint, Z_joint, R_angle)
        logger.instance().log(loggerMsg)  # 输出到logger中
        # logger.instance().log("Dobot Moving!")  # 输出到logger中
        dType.SetQueuedCmdStartExec(api)

    def SetRobotWait(self, RobotWaitTime):
        print("setRobotWait")
        dType.SetWAITCmd(api, RobotWaitTime, isQueued=1)
        loggerMsg = "Dobot setRobotWait! WaitTime:{}秒".format(RobotWaitTime)
        logger.instance().log(loggerMsg)  # 输出到logger中
        dType.SetQueuedCmdStartExec(api)

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
        velocityratio = getParams[0]
        logger.instance().log("Get dobot velocity ratio...")  # 输出到logger中
        return velocityratio

    def getPosition(self) -> float:
        print("Get robot position...")
        pos = dType.GetPose(api)
        position = []
        position = [pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7]]
        # time.sleep(0.5)
        logger.instance().log("Get dobot position...")  # 输出到logger中
        return position

    def stop(self):
        # print("stop")
        dType.SetQueuedCmdForceStopExec(api)
        dType.SetQueuedCmdStartExec(api)
        # logger.instance().log("Dobot stop!")  # 输出到logger中

    def start(self):
        print("start")
        dType.SetQueuedCmdStartExec(api)

    def reset(self):
        dType.SetQueuedCmdClear(api)
        logger.instance().log("Dobot reset!")  # 输出到logger中

    def get_alarm(self):
        dType.GetAlarmsState(api, 1000)

    def clear_alarm(self):
        dType.ClearAllAlarmsState(api)


def test_code() -> None:
    dobot_m1 = RobotImpl(3)
    dobot_m1.connect()
    dobot_m1.setVelocity(1, 1)
    dobot_m1.SetRobotWait(1)

    # dobot_m1.MoveToPoint(310.5333,-36.7193, 207.0039,-41.6406)
    dobot_m1.MoveToPoint(310.5333, 16.7193, 207.0039, -41.6406)
    dobot_m1.SetRobotWait(2)
    time.sleep(5)
    dobot_m1.stop()  # 测试紧急停止
    dobot_m1.StartExec()
    position = []
    position = dobot_m1.getPosition()
    print(position)

    time.sleep(5)
    dobot_m1.disconnect()


if __name__ == "__main__":
    test_code()
