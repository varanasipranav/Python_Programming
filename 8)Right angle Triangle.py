# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:02:11 2022

@author: Pranav Varanasi
"""

a=int(input("enter the first side"))
b=int(input("enter the 2nd side"))
c=int(input("enter the 3rd side"))
li=[a,b,c]
li.sort()
if li[2]**2==li[0]**2+li[1]**2:
    print("Right angle Triangle")
else:
    print("not a right angle trinangle")