# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:56:48 2021

@author: DELL
"""
#Clase 5
while True:
    x = input("Enter a number to count to:")
    if x == 'q' or x == 'quit':
        break

    x = int(x)
    y =1
    while True:
        y =1
        print(y)
        y=y+1
        if y>x:
            break