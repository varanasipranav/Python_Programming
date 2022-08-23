# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:51:34 2022

@author: Pranav Varanasi
"""


class Power:
    def __init__(self,n,x):
        self.n=n
        self.x=x
        
    def pow(self):
        return self.n**self.x
    
n=int(input())
x=int(input())
print(Power(n,x).pow())
    
    