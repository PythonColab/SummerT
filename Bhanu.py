# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:38:20 2018

@author: BHANU
"""
a=1
b=1
while(a!=0 or b!=0):
    a=input("Enter first Number")
    b=input("Enter Seacond Number")
    c=input("Enter The Operation")
    a=int(a)
    b=int(b)
    if(c=='+'):
        d=a+b
        print(d)
    elif(c=='-'):
        d=a-b
        print(d)
    elif(c=='*'):
        d=a*b
        print(d)
    elif(c=='/'):
        d=a/b
        print(d)
    else:
        print("Enter Proper Operation")