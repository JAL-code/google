# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# hoijui
# This module fails to work because linux_distribution DNE.

import os_identify
# format result
print(f"My OS: {os_identify.name()}")