# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 19:12:54 2021

@author: DELL
"""
def validarNumero(prompt, min, max):
    while(True):
        try:
            print("ingrese un valor entre",min,"y",max)
            x = int(input(prompt))
            assert x >= min and x <=max
            return x
        except ValueError:
            print('ingrese solo numeros')
        except:
            print("error, el valor debe estar dentro del rango")

v = validarNumero("ingrese un valor en el rango", -100,100)

print("el numero es: ", v)