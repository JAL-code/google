import sys

logfile=sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        print(line.strip())

#import re
#pattern = r"USER \((\w+)\)$"
#line = "Jul 6 14:04:01 computer.name CRON[29440]: (naughty_user)"
# $chmod +x check_cron.py
# $./check_cron.py sys
