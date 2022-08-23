# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:29:24 2022

@author: Pranav Varanasi
"""

class ItoR:
    def __init__(self):
        self.mapping=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    def Conv(self,num):
        roman=[]
        for i,numeral in self.mapping:
            while num>=i:
                num-=i
                roman.append(numeral)
                print(roman)
        print(''.join(roman))
n=int(input())
ItoR().Conv(n)
