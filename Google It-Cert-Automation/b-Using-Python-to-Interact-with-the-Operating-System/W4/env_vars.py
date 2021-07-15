#!/usr/bin/env python3
#A shell is a command line interface used to interact with your operating system"
#EX: Zsh Fish Bash(<-for Linux shell)
#environment variables 

#The commands:
#Echo: print text in Linux shell terminal  $Variable

import os

#Python
#os.environ dictionary to access environment variables in  Python
#.get([variable to find], [if var not found])  Method to access dictionary values in environ

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
