# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:39:53 2021

@author: DELL
"""
file = open('devices.txt')
for item in file:
    item = item.strip()
    print(item)
file.close()