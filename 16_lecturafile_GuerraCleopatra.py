# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:33:50 2021

@author: DELL
"""
'''
Abrir un archivo
'''

file = open('devices.txt','r')
for item in file:
    print(item)
file.close()