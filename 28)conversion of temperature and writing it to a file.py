# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:05:29 2022

@author: Pranav Varanasi
"""

f1=open("D:/GIT/Python/temp.txt",'r+')
f2=open("D:\GIT\Python\Far.txt",'r+')
l=f1.readlines()
li=[]
for i in l:
    t=int(i)
    li.append(t)
print(li)
far=[]
for i in li:
   temp=9/5*i+32
   far.append(temp)
print(far)
stli=[]
for i in far:
    t=str(i)
    stli.append(t)
print(stli)
st="\n".join(stli)
print(st)
f2.writelines(st)
f2.close()
f1.close

    
