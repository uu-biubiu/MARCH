# from enum import Enum
from __future__ import annotations
from abc import ABC, abstractmethod
#import Wrapper
import time
import Logger
from Precigenome.PGMFC import PGMFC

logger=Logger.Logger

class Pressure(ABC):
    # add more variables here!
    # make them protected by adding prefix "_"
    def __init__(self):
        pass

    def connect(self):
        pass
    def disconnect(self):
        pass
    def setPressure(self, airpressure, airchannel):
        pass
    def purgeOn(self, airchannel):
        pass
    def purgeOff(self, airchannel):
        pass
    def readPressure(self, airchannel) -> float:
        pass
    # add more interfac function here!

class PressureImpl(Pressure):
    def __init__(self):
        super().__init__()

    def connect(self, port):
        # instrument_serial_numbers = PGMFC.detect()
        # if not instrument_serial_numbers:
        #    raise Exception("No MFCS Series device detected")
        # print("\033[3;32mAvailable devices: {}\033[0m\n".format(instrument_serial_numbers))

        # Initialize the first instrument in the list
        # port = instrument_serial_numbers[0]
        # port = instrument_serial_numbers[len(instrument_serial_numbers) - 1]
        # print(len(instrument_serial_numbers))
        # print("Initialize {}".format(port))
        self.mfcs = PGMFC(port)

        # self.mfcs = PGMFC(instrument_serial_number)
        # print("Connected to Pressure Ctrl...")
        # print(self.mfcs)
        self.mfcs.monitor_start(span=100)
        logger.instance().log("Pressure Connected!")  # 输出到logger中
        # return pressure_connect_state

    def disconnect(self):
        self.mfcs.monitor_stop()
        logger.instance().log("Pressure Disconnected!")  # 输出到logger中

    def setPressure(self, airchannel, airpressure,runtime=600):
        #print("Set pressure...")
        #self._channelToPressure.update({airchannel: airpressure})
        #self.mfcs.set_params(channel=airchannel, peak=airpressure, runtime=600)
        self.mfcs.set_params(channel=airchannel, peak=airpressure,runtime=runtime)
        loggerMsg = "Set pressure... airchannel:{} airpressure:{}".format(airchannel, airpressure)
        logger.instance().log(loggerMsg)  # 输出到logger中

    def purgeOn(self, airchannel):
        #print("Start running...")
        self.mfcs.purge_on(airchannel)
        logger.instance().log("Start running...")  # 输出到logger中

    def purgeOff(self, airchannel):
        #print("Stop running...")
        self.mfcs.purge_off(airchannel)
        logger.instance().log("Stop running...")  # 输出到logger中

    def readPressure(self, airchannel) -> float:
        #print("Get pressure...")
        print(self.mfcs.get_pressure(airchannel))
        return self.mfcs.get_pressure(airchannel)[0]
        logger.instance().log("Get pressure...")  # 输出到logger中
        # add more function implementation here!


def test_code() -> None:
    if len(PGMFC.detect())==2:
        precigenome_claw = PressureImpl()  # 控制夹爪的流控仪
        #夹爪开闭测试
        precigenome_claw.connect()

        precigenome_claw.setPressure(1, 10)
        precigenome_claw.purgeOn(1)
        time.sleep(5)
        precigenome_claw.purgeOff(1)
        time.sleep(1)

        precigenome_claw.setPressure(1, -10)
        precigenome_claw.purgeOn(1)
        time.sleep(5)
        precigenome_claw.purgeOff(1)
        time.sleep(1)

        precigenome_claw.disconnect()


        #芯片气路测试
        precigenome_chip = PressureImpl()   # 控制芯片的流控仪
        precigenome_chip .connect()

        precigenome_chip.setPressure(1, 10)
        precigenome_chip.purgeOn(1)
        time.sleep(5)
        precigenome_chip.purgeOff(1)
        time.sleep(1)

        precigenome_chip.setPressure(1, -10)
        precigenome_chip.purgeOn(1)
        print(precigenome_chip.readPressure(1))
        time.sleep(5)
        precigenome_chip.purgeOff(1)
        time.sleep(1)

        precigenome_chip.disconnect()
    else:
        print("请保证连接两台流控仪！")



if __name__ == "__main__":
    test_code()

