# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:49:23 2022

@author: Pranav Varanasi
"""

lower=1
upper=20
for i in range(upper):
        if all(i%j!=0 for j in range(2,i)):
            print(i)
            