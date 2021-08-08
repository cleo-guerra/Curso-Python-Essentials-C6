# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:10:37 2021

@author: DELL
"""

'''
Excepciones 

'''
import math

x = float(input('Enter x:'))
y = math.sqrt(x)
print('The square root of:',x,'equals to',y)

try:
    print('1')
    x=1/0
    print('2')
    
except:
    print('oh dear, something went wrong')
    
print('3')

try:
    x=int(input("enter a number:"))
    y=1/x
    print('valor: ',y)
except ZeroDivisionError:
    print('You can not divide by zero, sorry')
    
except ValueError:
    print("you must enter an integer value")
    
except: 
    print('oh dear, something went wrong')
    
print('the end')

try:
    y=1/0
except ZeroDivisionError:
    print("Zero Division")
    
except ArithmeticError:
    print('Aritmethic problem')
print("end")