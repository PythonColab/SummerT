# -*- coding: utf-8 -*-
"""
Created on Wed May 16 08:46:02 2018

@author: BHANU
"""

a=["Hello",1,2,4.6]
c='y'
while(c=='y'):
    c=input("Input some varaible : ")
    a.append(c)
    for i in a:
        print(a[i])