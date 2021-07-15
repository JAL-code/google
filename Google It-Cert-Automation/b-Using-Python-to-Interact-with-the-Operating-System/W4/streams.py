#!/usr/bin/env python3

#I/O Streams - the ways for programs to get and receive information.
#This file is a demostration of  I/O Streams - the basic mechanism, or pathways,  for performing input, keyboard,  and output, screen,  operations in your programs
#3 Types of Streams - the data keeps flowing

#STDIN or standard input from keyboard (text data) to program.  Function input()
data = input("This will come from STDIN: ")

#STDOUT or standard output from program to screen (text on screen in terminal). Function print()
print("Now we write it to STDOUT: " + data)

#STDERR or stamdard error channel to show messages and diagnostics.  Again from program to screen.
print("Now we generate an error to STDERR: " + data +  1)
