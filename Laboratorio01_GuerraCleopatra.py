# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:05:47 2021

@author: DELL - Guerra Cleopatra
"""
'''
Crear un código en el editor que asigna un valor flotante, 
lo coloca en una variable llamada x, e imprime el valor de 
la variable llamada y. 
Su tarea es completar el código para evaluar la siguiente expresión:

3x^3 - 2x^2 + 3x - 1

'''

#Forma 1

'''
Se pide ingresar el valor de x para evaluar la funcion
y definida y almacenada en la variabel y

'''
x = float(input('Ingresa el valor de x:'))

#y = 3*x*x*x - 2*x*x + 3*x - 1
y = 3*pow(x,3) - 2*pow(x,2) + 3*pow(x,1) -1

print('Al evaluar la expresion 3x^3 - 2x^2 + 3x - 1, para un valor de x=', x,' obtengo y= ',y,'\n')

print('La expresion es de tipo: ',type(y),'\n')

#Otra forma directa con variable definidas sin ingreso de teclado

s = float(0)
t = 3*s*s*s - 2*s*s + 3*s - 1
print('La expresión evaluada para s=  ',s,'en t es: ',t,'de tipo',type(t),'\n')


s = float(1)
t = 3*s*s*s - 2*s*s + 3*s - 1
print('La expresión evaluada para s=  ',s,'en t es: ',t,'de tipo',type(t),'\n')

s = float(-1)
t = 3*s*s*s - 2*s*s + 3*s - 1
print('La expresión evaluada para s=  ',s,'en t es: ',t,'de tipo',type(t),'\n')

