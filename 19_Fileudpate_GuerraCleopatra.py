# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:46:26 2021

@author: DELL
"""
file = open("devices.txt", "a")
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()