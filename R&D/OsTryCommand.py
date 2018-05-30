# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:44:52 2018

@author: BHANU
"""

import os
import msvcrt
command = " "
while (command != "exit"):
    command = input("Command: ")
    handle = os.popen(command)
    line = " "
    while line:
        line = handle.read()
        print(line)
    handle.close()

print("Ciao that's it!")