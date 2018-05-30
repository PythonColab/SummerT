# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:37:03 2018

@author: BHANU
"""

import os
import msvcrt
import subprocess

cmd = "date"

# returns output as byte string
returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
print('Current date is:', returned_output.decode("utf-8"))
