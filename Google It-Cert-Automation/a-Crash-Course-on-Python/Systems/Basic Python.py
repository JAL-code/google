#!/user/bin/env python38

#Save as chmod +x health_checks.py
#./he
#./health_checks.py

import shutil #disk usage
import psutil #processor usage

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is okay")

du = shutil.disk_usage("/")
print(du)

print(du.free/du.total)

print(psutil.cpu_percent(0.1))