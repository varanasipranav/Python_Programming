# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:21:06 2022

@author: Pranav Varanasi
"""
import math
from collections import namedtuple
def Collision(b1,b2):
    dist=math.dist([b1.x,b1.y],[b2.x,b2.y])
    if dist>r1+r2:
        print("No Collision")
    else:
        print("coliision")


x1=int(input("enter x1"))
y1=int(input("enter y1"))
r1=int(input("enter r1"))
x2=int(input("enter x2"))
y2=int(input("enter y2"))
r2=int(input("enter r2"))
ball=namedtuple("Ball", ['x','y','r'])
b1=ball(x1,y1,r1)
b2=ball(x2,y2,r2)
Collision(b1, b2)
