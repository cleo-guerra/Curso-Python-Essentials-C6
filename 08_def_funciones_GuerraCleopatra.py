# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:28:09 2021

@author: DELL
"""
#funciones
def message():
    print ('enter next value')
print('We start here')
message()
print("The end is here")

def hi(name):
    print("Hi",name)
    
hi('cleo')

def saludo():
    print("hola")
    
saludo()
hi('cleo')

def suma(x,y):
    x = int(input("ingrese x:"))
    y = int(input("ingrese y:"))
    c = x + y
    print(c)
    
suma(1,5)

def saludos(nombre1, nombre2):
    print("hola", nombre1, nombre2)
    
saludos("cleo", "yoma")

def direccion(provincia,ciudad,barrio):
    print('su dereccion es:')
    print('su provincia es:',provincia)
    print('La ciudad de domicilio es:', ciudad)
    print('la direccion de referencia es:',barrio)
    
prv= input('ingrese la provincia')
bar=input('ingrese el barrio')
ci=input('ingrese la ciudad')

direccion(prv,ci,bar)
#otra forma
direccion(provincia = prv, ciudad=ci, barrio=bar)