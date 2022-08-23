# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:07:34 2022

@author: Pranav Varanasi
"""

st=input()
li=["pranav"," ","Bad"," boy"]
print(st.split())
print("".join(li))
d={'pranav':{'birthday':'10-10-2002'},'Shyam':{'birthday':'22-9-2002'},'Surya':{'birthday':'26-1-2002'},'Kareem':{'birthday':'9-05-2002'}}
name=input("enter the name")
print(d[name]['birthday'])