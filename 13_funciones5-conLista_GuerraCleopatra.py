# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:25:11 2021

@author: DELL
"""
def saludos(lista):
    for puntero in lista:
        print('hola,',puntero)
    print("")
    
saludos(['Juan'])
saludos(['Cleo','Yomara'])
saludos(['Ana','Mik','Narcy'])


def createList(n):
    lista =[]
    for i in range(n):
        lista.append(i)
    return lista

print(createList(5))
    