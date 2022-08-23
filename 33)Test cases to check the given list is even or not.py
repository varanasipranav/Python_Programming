# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:56:44 2022

@author: Pranav Varanasi
"""

while(True):
    li=list(map(int,input("enter the list").strip().split()))
    if all (i%2==0 for i in li):
        print("all are even")
    else:
        print("Not all are even")
    print("Do you want another test case Y/N")
    ch=input()
    if ch=='N':
        break
    else:
        continue