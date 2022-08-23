# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:50:36 2022

@author: Pranav Varanasi
"""

t=int(input("enter the test cases"))
while(t>0):
    st=input("enter the string")
    l=list(st)
    l.reverse()
    s="".join(l)
    print(s)
    t=t-1
