# from enum import Enum
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import inspect
import ntpath

class LoggerBase(ABC):
    # add more variables here!
    # make them protected by adding prefix "_"
    def __init__(self):
        pass
    # add more interfac function here!


class Logger():
    _instance = None

    def __init__(self, path: str):
        super().__init__()
        self._path = path
        # self.__file=open(path,"w+")

    @staticmethod
    def instance() -> Logger:
        if (Logger._instance is None):
            Logger._instance = Logger("../logs/control.log")
        return Logger._instance


    def __enter__(self):
        return self

    # def __exit__(self, exc_type, exc_value, traceback):
    # self.__file.close()
    def log(self, logMsg: str):
        func = inspect.currentframe().f_back.f_code
        head, tail = ntpath.split(func.co_filename)
        dateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(logMsg)
        newMsg = "{} 调用{}()中{}函数: {}\n".format(dateTime, tail, func.co_name, logMsg)
        file = open(self._path, "a+")
        file.writelines(newMsg)
        file.close()

    def path(self) -> str:
        return self._path


def test_code() -> None:
    #logger = Logger("control2.log")
    #logger.log("22222!")
    Logger.instance().log("First logger msg!")


if __name__ == "__main__":
    test_code()
