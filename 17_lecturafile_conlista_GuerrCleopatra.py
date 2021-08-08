# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:41:20 2021

@author: DELL
"""

devices = []
file = open('devices.txt','r')
for item in file:
    item = item.strip()
    devices.append(item)

file.close()
print(devices)