# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:13:09 2022

@author: Pranav Varanasi
"""
file1=input("enter the first file name")
file2=input("enter the second file name")
f1=open(f"D:\GIT\Python\{file1}",'r+')
f2=open(f"D:\GIT\Python\{file2}",'r+')
li=f1.readlines()
st="".join(li)
f2.writelines(st)
f2.close()
f1.close()