#!/usr/bin/env python3

import os
import shutil
import psutil
# pip install psutil
import sys
import socket
import emails

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_percent):
    """Returns True if there is not enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free/du.total
    if percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_percent=20)

def check_memory():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024
    if mem.available <= THRESHOLD:
        return True
    return False

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    if usage < 80:
        return True
    return False

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname('localhost')
    except sys.error:
        return True

def main():
    checks = [
              (check_reboot, "Error - Pending Reboot"),
              (check_cpu_usage, "Error - CPU usage is over 80%"),
              (check_root_full, "Error - Available disk space is less than 20%"),
              (check_memory, "Error - Available memory is less than 500MB"),
              (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1")
	         ]
    everything_ok = True
    for check, msg in checks:
        if check():
            # TODO: send the user the warning about the check failure
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = msg
            body = "Please check your system and resolve the issue as soon as possible."
            message = emails.generate_email(sender, receiver, subject, body, "none")
            emails.send_email(message)
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()