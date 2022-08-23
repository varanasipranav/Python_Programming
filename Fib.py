# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:08:33 2022

@author: Pranav Varanasi
"""

def Fib(n):
    if n==0:
        return 0;
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
