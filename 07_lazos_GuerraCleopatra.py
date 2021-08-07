# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:00:59 2021

@author: DELL
"""
## el archivo se llama 04.. tiene solo el if
'''
04_GuerraCleopatra_
'''
print('Inicio')
nativeVLAN = 10
dataVLAN = 100

print("Antes del IF")

if nativeVLAN == dataVLAN:
    print('dentro del IF para el valor de verdad')
    print("The native Vlan and the dataVLAN are the same.")
else:
    print("dentro del ELSE para el valor falso")
    print("This native VLAN and the data are different.")

print("Despues del IF")
print("Fin")

#elif en el archivo archivo 5 con el for

aclNum = int(input('What is the IPv4 ACL number?'))
if aclNum >= 1 and aclNum <= 99:
    print("la ACL es estandar")
elif aclNum >= 100 and aclNum <= 199:
    print("La ACL es extendida")
else:
    print("EL numero ingresado no es de un ACL")
    
#for al conocer las veces k se van a ejecutar en este.

#
print("Inicio")
devices=["R1",'R2',"R3","S1","S2"]
for item in devices:
    print(item)
print("Fin")

for item in devices:
    if "R" in item:
        print(item)
        
        
lista1=[]       
for item in devices:
    if "S" in item:
        lista1.append(item)
print(lista1)

lista2=[]
for item in devices:
    if "R" in item:
        lista2.append(item)
print(lista2)

#otra forma
lista_r=[]
lista_s=[]

for item in devices:
    if 'R' in item:
        lista_r.append(item)
    else:
        lista_s.append(item)
print(lista_r)
print(lista_s)

