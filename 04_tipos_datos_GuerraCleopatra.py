# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:15:01 2021

@author: DELL
"""
#clase 3 -2021-07/29

#para imprimir el tipo de datos
a = 5

print (type(a))

print('Tipos de Datos:\n')
print(type(5.2))
print(type(5))
print(type(True))
print(type('cleo'))

#Operadores Booleanos

print('Operadores:\n')
b=1
c=2
print(b<c)
print(b>c)
print(b==c)
print(b!=c)
print(b>=c)
print(b<=c)

#ejercicio
print('Ejemplo:\n')
x = 5
y= x+3
print(y)

t = 'Cleo'*y
print(t)

#Salto de lnea
print('dos saltos de lines','\n'*2)
n = 'yoma'
print(n)

str1 = 'Cisco'
str2 = 'Networking'
str3 = 'Academy'
space=' '
print(str1+space+str2+space+str3)
print(str1+str2+str3)
print(str1,str2,str3)

x = 5
print('El valor de x es:', x)


#concatenacion
print('El valor de x es:'+ str(x))
print(type(x))
#conversion de tipo de datos
x = str(x)
print(type(x))

x = int(x)
print(type(x))

x = float(x)
print(type(x))

x = bool(x)
print(type(x))

#formato de ipresion
pi = 22/7
print(pi)
print('{:.5f}'.format(pi))
#el limite es hasta 50, los demas los llena de 0s
print('{:.51f}'.format(pi))
print('{:.55f}'.format(pi))
