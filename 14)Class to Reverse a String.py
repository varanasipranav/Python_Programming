# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:01:09 2022

@author: Pranav Varanasi
"""

class A:
    def __init__(self,st):
        self.st=st
    def reverse(self):
        li=list(self.st)
        li.reverse()
        st1="".join(li)
        return st1
st=input("enter the string")
print(A(st).reverse())
        