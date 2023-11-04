# This program is for 2 refill modes: always-on refill and pulse refill

# from enum import Enum
from __future__ import annotations
# from abc import ABC, abstractmethod
# import Wrapper
import binascii
import datetime
import serial
import serial.tools.list_ports
import time
import struct


global ser
class ValveImplArduino():
    def __init__(self):
        super().__init__()

    def connect(self,PORT)->int:
        valve_connect_state=0  #电磁阀未连接
        global ser
        print("Connected to Valve Ctrl...")
        ser = serial.Serial(port=PORT, baudrate=115200, timeout=0.5)
        time_connect = datetime.datetime.now()
        print(str(time_connect))
        while (1):
            # 从串口读取数据
            data = ser.read().decode('gbk')
            #print(data)
            #print(type(data))
            time_receive = datetime.datetime.now()
            print(time_receive)
            total_seconds = (time_receive - time_connect).total_seconds()
            print(total_seconds)

            if total_seconds>=2:
                break

            if data == "1":
                print("电磁阀连接成功")
                valve_connect_state = 1  # 电磁阀已连接
                break
            #print("电磁阀连接失败")

        print(valve_connect_state)
        return valve_connect_state

    def disconnect(self):
        global ser
        print("Disconnected from Valve Ctrl...")
        ser.close()

    def setPrinting(self, frequency, PulseTime, RefillTime, PulseCount, AlwaysOn):
        print("Set Valve...")
        single_Ctrl = [255, 255]
        single_Ctrl.append(frequency)
        single_Ctrl.append(PulseTime%256)
        single_Ctrl.append(PulseTime//256)
        single_Ctrl.append(RefillTime%256)
        single_Ctrl.append(RefillTime//256)
        single_Ctrl.append(PulseCount%256)
        single_Ctrl.append(PulseCount//256)
        single_Ctrl.append(AlwaysOn)
        out = ser.write(single_Ctrl)
        time.sleep(0.10)
        # time.sleep(0.25)
        # add implementation here!
    # add more function implementation here!

    def SwitchState(self, switchstate):
        print("Swich On Valve...")
        single_Ctrl = []
        if switchstate:
            single_Ctrl = [255, 255, 239, 239, 0]
        else:
            single_Ctrl = [255, 255, 254, 254, 0]
        out = ser.write(single_Ctrl + single_Ctrl)
        # time.sleep(0.1)

    def ValveState(self, pin, switchstate):
        global ser
        single_Ctrl = []
        if switchstate:
            print("Turn On Valve...")
            single_Ctrl = [255, 255, 245, 245, pin, 0]
        else:
            print("Turn Off Valve...")
            single_Ctrl = [255, 255, 240, 240, 0]
        out = ser.write(single_Ctrl + single_Ctrl)


class ValveImpl():
    #   Arduino=1
    _impl = 0
    def __init__(self):
        super().__init__()
        self._impl = ValveImplArduino()
    def connect(self,PORT)->int:
        return self._impl.connect(PORT)
    def disconnect(self):
        self._impl.disconnect()
    def SwitchState(self, switchstate):
        self._impl.SwitchState(switchstate)
    def ValveState(self, pin, switchstate):
        self._impl.ValveState(pin, switchstate)
    def setPrinting(self, frequency, PulseTime, RefillTime, PulseCount, AlwaysOn):
        self._impl.setPrinting(frequency, PulseTime, RefillTime, PulseCount, AlwaysOn)



def test_code() -> None:
    rWrpper = ValveImpl()
    rWrpper.connect("com3")
    time.sleep(3)
    rWrpper.ValveState(2, 1)
    time.sleep(3)
    rWrpper.ValveState(2, 0)
    time.sleep(1)
    rWrpper.setPrinting(5, 50, 10, 10, 1)
    rWrpper.SwitchState(1)
    time.sleep(10)
    rWrpper.SwitchState(0)
    time.sleep(1)

    rWrpper.disconnect()


if __name__ == "__main__":
    test_code()



