# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:31:20 2022

@author: Pranav Varanasi
"""
#10A B C
import numpy as np
l=list(map(int,input("enter the numbers in order").strip().split()))
a=np.matrix(l)
a=a.reshape(3,3)
li=list(map(int,input("enter the numbers in order").strip().split()))
b=np.matrix(l)
b=b.reshape(3,3)
print(a+b)
print(a*b)

