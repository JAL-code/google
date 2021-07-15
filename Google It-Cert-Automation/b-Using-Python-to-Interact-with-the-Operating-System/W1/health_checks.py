import shutil
import psutil

'''
Detect dangerously high CPU usage levels across a network 
and scale back the CPU clock speeds of those devices,
or shut them down to prevent overheating
'''


def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def print_disk_usage():
  du_parent = shutil.disk_usage("/")
  return du_parent

def print_cpu_percent(seconds):
  return psutil.cpu_percent(seconds)

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
  print("ERROR!")
else:
  print("Everything is OK!")
  print(print_disk_usage())
  print("10% load: {}".format(print_cpu_percent(10)))
