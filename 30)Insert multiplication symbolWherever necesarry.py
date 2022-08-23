# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:40:30 2022

@author: Pranav Varanasi
"""

str1=input("Enter an algebraic expression:")
str2=""
for i in range(len(str1)):
    if(str1[i].isdigit() and str1[i+1]=='('):
        str2=str2+str1[i]+'*'
    elif(str1[i].isdigit() and str1[i+1].isalpha()):
        str2=str2+str1[i]+'*'
    else:
        str2=str2+str1[i]
print(str2)