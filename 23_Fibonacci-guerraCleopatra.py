# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 20:13:01 2021

@author: DELL
"""

def fibonacci(n):
    a= 0
    b= 1
    while a < n:
        print(a)
        a, b = b, a+b
    print()
    
