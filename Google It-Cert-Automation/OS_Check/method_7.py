# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# Memin

import platform
from enum import Enum

class OS(Enum):
    def checkPlatform(osName):
        return osName.lower() == platform.system().lower()

    MAC = checkPlatform("darwin")
    LINUX = checkPlatform("linux")
    WINDOWS = checkPlatform("windows")

if OS.LINUX.value:
    print("Linux OS")
if OS.MAC.value:
    print("MAC")
if OS.WINDOWS.value:
    print("Windows")