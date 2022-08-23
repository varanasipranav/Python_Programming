# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:55:19 2022

@author: Pranav Varanasi
"""

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)



n=int(input("enter the number for which you need fact"))
print(fact(n))