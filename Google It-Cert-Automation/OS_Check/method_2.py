# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# coldfix

from __future__ import print_function
import os
import sys
import platform
import sysconfig

# Added string formatting
print(f"os.name                 : {os.name}")
print(f"sys.platform            : {sys.platform}")
print(f"platform.system()       : {platform.system()}")
print(f"sysconfig.get_platform(): {sysconfig.get_platform()}")
print(f"platform.machine()      : {platform.machine()}")
print(f"platform.architecture() : {platform.architecture()}")
