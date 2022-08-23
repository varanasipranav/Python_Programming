# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:18:03 2022

@author: Pranav Varanasi
"""
f1=open("D:\GIT\Python\File1.txt",'r+')
li=f1.readlines()
st="".join(li)
d={}
for i in st:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)