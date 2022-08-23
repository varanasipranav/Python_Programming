# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:19:44 2022

@author: Pranav Varanasi
"""


f1=open("D:\GIT\Python\File1.txt",'r+')
li=f1.readlines()
print(li)
st="".join(li)
li1=st.split()
print(li1)
s=set(li1)
l=list(s)
l.sort()
print(l)