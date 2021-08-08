# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 11:41:36 2021

@author: DELL
"""
floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas']
floor_numbers = range(-1,4)

class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:
            print('El piso de {} es el número: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('No hay ningún piso de {} en este edificio.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
            print('Vaya al piso {} es: {}.'.format(floor_number, self._number_to_type_dict[floor_number]))
        else:
            print('En este edificio esta el piso {}'.format(floor_number))
           


el = Elevator(floor_numbers, floor_types)

el.go_to_floor(1)
el.go_to_floor(-2)
el.ask_which_floor('Oficinas')
el.ask_which_floor('Swimming Pool')