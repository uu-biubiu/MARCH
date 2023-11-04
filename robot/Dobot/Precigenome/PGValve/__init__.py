# -*- coding: utf-8 -*-
import time
"""Module for communicating with selecting valves or switching valves"""
# from . import control_c as controller
from Precigenome.PGValve import control_c as controller

# from . import utils
from Precigenome.PGValve import utils
from Precigenome.PGValve.exceptions import VALVES_Unknown, VALVES_AckError, VALVES_InvalidType

class PGValve(object):
    """Represents an valve device, allowing the user to operate or read settings"""

    @staticmethod
    def detect():
        """Returns a list containing the serial numbers of all available valve devices"""
        print('detect start...')
        c_error, list_valves, list_types, list_mountids = controller.detect()
        return list_valves, list_types, list_mountids

    def __init__(self, serial_number=0, valvetype=1, mountid=1, bAutoDetect=False):
        """Creates an object that respresents the valve device"""
        # Check if there are devices connected, and raise an exception if not
        if bAutoDetect:
            available_devices, valvetype_list, mountid_list = PGValve.detect()
            if not available_devices:
                utils.parse_error(101)
                self.__handle = 0
                raise VALVES_InvalidType("no valid")
            if serial_number != 0 and serial_number not in available_devices:
                utils.parse_error(101)
                raise VALVES_InvalidType("the specified port is not in available")

            if available_devices:
                serial_number = available_devices[0]
                valvetype = valvetype_list[0]
                mountid = mountid_list[0]
                time.sleep(0.02)

        self.__handle = controller.initialize(serial_number, valvetype, mountid)

        if not self.__handle:
            time.sleep(0.1)
            self.__handle = controller.initialize(serial_number, valvetype, mountid)

        if not self.__handle:
            utils.parse_error(101)
            self.__handle = 0
            raise VALVES_InvalidType("Initialize Fail")

        return

    def close(self):
        """terminates threads and deallocates memory used by this session"""
        if self.__handle != 0:
            controller.close(self.__handle)
            self.__handle = 0

        return
    
    def reset(self):
        return controller.reset(self.__handle)

    def querycurpos(self):
        """query current location"""
        c_error, curpos = controller.querycurpos(self.__handle)
        utils.parse_error(c_error)
        return curpos

    def switchto(self, port):
        """switch to """
        c_error = controller.switchto(self.__handle, port)
        utils.parse_error(c_error)
        return

    def getonecirclecount(self):
        """read total ports"""
        c_error, count = controller.getonecirclecount(self.__handle)
        utils.parse_error(c_error)
        return count

    def getversion(self):
        """read module id"""
        c_error, vid = controller.getversion(self.__handle)
        utils.parse_error(c_error)
        return vid

    def ispoweronreset(self):
        """query if auto reset after poweron"""
        c_error, isautoreset = controller.ispoweronreset(self.__handle)
        utils.parse_error(c_error)
        return isautoreset

    def setpoweronreset(self, isautoreset):
        """set"""
        c_error = controller.setpoweronreset(self.__handle, isautoreset)
        utils.parse_error(c_error)
        return

    def getmaxrpm(self):
        """query max speed."""
        c_error, maxrpm = controller.getmaxrpm(self.__handle)
        utils.parse_error(c_error)
        return maxrpm

    def setmaxrpm(self, maxrpm):
        """set max speed. 50-350"""
        c_error = controller.setmaxrpm(self.__handle, maxrpm)
        utils.parse_error(c_error)
        return

    def getresetspeed(self):
        """query reset speed."""
        c_error, speed = controller.getresetspeed(self.__handle)
        utils.parse_error(c_error)
        return speed

    def setresetspeed(self, speed):
        """set reset speed. 50-350"""
        c_error = controller.setresetspeed(self.__handle, speed)
        utils.parse_error(c_error)
        return

