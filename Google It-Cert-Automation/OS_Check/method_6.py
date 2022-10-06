# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# tudor

import sys

def get_os(osoptions={'linux':'linux','Windows':'win','macos': 'darwin'}):
    # get OS to allow code specifics

    opsys = [k for k in osoptions.keys() if sys.platform.lower().find(osoptions[k].lower()) != -1]
    try: 
        return opsys[0]
    except:
        return 'unknown_OS'

# Added call 
if __name__ == '__main__':
    # Get OS
    print(get_os())
    # Check Platform
    print(sys.platform)