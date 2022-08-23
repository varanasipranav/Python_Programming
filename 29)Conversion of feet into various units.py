# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:27:59 2022

@author: Pranav Varanasi
"""
helper = [[1, 'feets-inches', 12],
          [2, 'feets-yards', 0.33333],
          [3, 'feets-miles', 0.000189393939],
          [4, 'feets-millimeters', 304.8],
          [5, 'feets-centimeters', 30.48],
          [6, 'feets-meters', 0.3048],
          [7, 'feets-kilometers', 0.0003048]]
for i in range(0,7):
    print(i+1,helper[i][1])
ch=int(input("enter the choice"))
feet=int(input("enter the amount in feets"))
print("index    Conversion     Value")
for i in range(0,7):
    print(i+1,"    ",helper[i][1],"     ",feet*helper[i][2])