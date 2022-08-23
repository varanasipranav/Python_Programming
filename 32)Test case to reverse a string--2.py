# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:53:49 2022

@author: Pranav Varanasi
"""

while(True):
    st=input("enter the string")
    li=list(st)
    li.reverse()
    s="".join(li)
    print(s)
    print("Do you want another test case Y/N")
    ch=input()
    if ch=='N':
        break
    else:
        continue