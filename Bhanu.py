# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:38:20 2018

@author: BHANU
"""
f=open("E:\Study\Calc.txt","r+")
while(a!=0 or b!=0):
    for line in f:
        line=line.split(' ')
        a=int(line[0])
        b=int(line[2])
        c=int(line[1])
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
