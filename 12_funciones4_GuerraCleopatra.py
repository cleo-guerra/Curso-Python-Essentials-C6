# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:44:48 2021

@author: DELL
"""
#Funcion Suma
print('Operaciones \n')

def Suma(a,b):
    return(a + b)

suma=Suma(2,3)
print('El resultado de la suma es: ',suma,'\n')

def Resta(a,b):
    return(a - b)

resta=Resta(2,3)
print('El resultado de la resta es: ',resta,'\n')

def Multiplicacion(a,b):
    return(a * b)

mul=Multiplicacion(2,3)
print('El resultado de la multiplicacion es: ',mul,'\n')

def Division(a,b):
    return(a / b)

div=Division(10,3)

print('El resultado de la division es: ',"{0:.3f}".format(div),'\n')

def Potencia(a,b):
    return(pow(a, b))

pot=Potencia(2,3)
print('El resultado de la potencia es: ',pot,'\n')


