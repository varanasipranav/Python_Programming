# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:44:06 2022

@author: Pranav Varanasi
"""

print("1) Cel to Faren \n 2)Faren to Cel")
ch=float(input("enter the choice"))
if ch==1:
    cel=int(input("Enter the Temp in celcius"))
    faren=(9/5)*cel+32
    print("the temperature in farenheit is",faren)
elif ch==2:
    faren=float(input("enter the temp in faren"))
    cel=((faren-32)/9)*5
    print(cel)
