import re
#import subprocess

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

regex = r"([a-zA-Z]+ \d+ \d+:\d+:\d+).*\[(\d+)\]\:"#\[(\d+(\]"
result = re.search(regex, log)  #the magic
print(result[1], result[2])
#regular expression
