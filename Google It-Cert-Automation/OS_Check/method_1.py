# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# Stefan Gruenwald

import platform

print(dir(platform))
for x in dir(platform):
    if x[0].isalnum():
        try:
            result = getattr(platform, x)()
            # Improved output (added)
            print(f"{platform}.{x}.{result}")
        except TypeError:
            continue
        # Check for OSError (added)
        except OSError:
            continue