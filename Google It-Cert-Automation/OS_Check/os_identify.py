# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# hoijui
# module for method 5.  This module fails to work.
import platform
from platform import distribution
from platform import win32_ver
from platform import mac_ver

def is_linux():
    try:
        platform.linux_distribution()
        return True
    except:
        return False

def is_windows():
    try:
        platform.win32_ver()
        return True
    except:
        return False

def is_mac():
    try:
        platform.mac_ver()
        return True
    except:
        return False

def name():
    if is_linux():
        return "Linux"
    elif is_windows():
        return "Windows"
    elif is_mac():
        return "Mac"
    else:
        return "<unknown>"