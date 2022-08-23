# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:22:50 2022

@author: Pranav Varanasi
"""

f1=open("D:\GIT\Python\email.txt",'r+')
l=f1.readlines()
st="".join(l)
print(st)
li=st.split("\n")
print(li)
s=";".join(li)
print(s)