# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:27:08 2022

@author: Pranav Varanasi
"""

li=list(map(int,input("enter the list").strip().split()))
l=[]
def dup(li):
    l=[]
    for i in li:
        if li.count(i)==1:
            l.append(i)
    s=set(l)
    l1=list(s)
    print(l1)
dup(li)
            
    