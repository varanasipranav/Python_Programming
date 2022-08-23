# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:31:20 2022

@author: Pranav Varanasi
"""
#10 A B C
import numpy as np
a=np.matrix('1,1,1;1,1,1;1,1,1')
print(a)
b=np.zeros((3,3))
print(b)
c=np.ones((3,3))
print(c)
d=np.eye(3)
print(d)
print(a+c)
print(a*d)