# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# G M

import platform

print(f"Default test: {platform.os.name}")
print(f"Uname test  : {platform.uname()}")

for i in zip(['system', 
              'node', 
              'release', 
              'version', 
              'machine', 
              'processor'], platform.uname()):
    # Add print
    print(f"{i[0]}: {i[1]}")
