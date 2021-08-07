# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:12:30 2021

@author: DELL
"""

'''
no hay vectores y matrices coomo tal
tuplas y listas son casi iguales la diferencia es la mutabilidad(no se modifica la informacion) en una tupla
'''

#lista
#devuelven la indexizacion tanto listas como tuplas
#tuplas
'''
una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. 
Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas. Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía
'''
#diccionario

'''
almacena valores no indexados, no soporta valores repetidos de llave

'''

#mutable e inmutable de la inf

"""
listas almacenan inf
se declaran en corchetes
en las listas y tuplas almacenan diferentes tipos de datos como int, floar, string, booleanos en una misma lista
las tuplas se declaran en ()
veo type y da el valor 
empleo la funcion len() para ael tamano
almacenan valores repetidos
emplean indezacion
los valores de la tupla no se pueden eliminar
 

"""

#lista vacia
lista=['R1', 5, True, 0.85,0.85]
print(type(lista))
print(lista)
print(len(lista),'\n')

#tupla
tupla=['R1', 5, True, 0.85,0.85]
print(type(tupla))
print(tupla)
print(len(tupla),'\n')

#emplean indezacion
print(lista[0])
print(tupla[2])
print(lista[-1])
print(lista[-3])

#en las listas puedo modificar la inf
#en las tuplas no se modifican sus datos

lista[0] = 'mod'
print(lista)

#eliminar de la lista
del lista[4]
print(lista)

lista.append('nuevo')
print(lista,'\n')

#diccionarios
'''
son un conjunto de datos no ordenados
es decir no tienen indexacion
se tiene una llave ya no se llama a los indices para recuperar los valores
sino k llamo a la llave
la declaracion es con {}
No SOPORTA VALORES REPETIDOS LA LLAVE NO SE PEUEDE REPETIR, se queda con el ultio valor que se asigna

'''

dict1 = {'R1':"10.10.10.1",
         1: "Cleo Guerra",
         "R2": "10.10.10.2",
         True:"10.10.10.3"
         }

print(dict1)

dict2 = {'R1':"10.10.10.1",
         12: "Cleo Guerra",
         "R2": "10.10.10.6",
         True:"10.10.10.3",
         'R1':"10.10.10.5"
         }

print(dict2)
print(type(dict2))
print(dict2[12])
print(dict2['R2'])
print('S1' in dict1)


