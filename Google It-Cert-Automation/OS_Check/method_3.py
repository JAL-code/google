# Stack Overflow: questions/1854/how-to-identify-on-which-os-python-is-running-on/58071295#58071295
# urantialife

# Clears the terminal if os is found
def cls():
    from subprocess import call
    from platform import system
    type = 'unknown'
    os = system()
    if os == 'Linux':
        type = 'Linux'
        call('clear', shell = True)
    elif os == 'Windows':
        type = 'Windows'
        call('cls', shell = True)
    return type

# Added call to function. 
print(cls())