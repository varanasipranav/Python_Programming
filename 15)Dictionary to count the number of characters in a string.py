# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:04:23 2022

@author: Pranav Varanasi
"""

st=input("enter a String")
d={}
for i in st:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)