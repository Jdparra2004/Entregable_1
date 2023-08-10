'''
Created on Sun Agu 6 10:30 pm

@author: Jaidi

2023_Retos1_Elementos_Programacion: Problema 6

Caso pH

Condiciones Iniciales:
    Se solicitará al usaurio la concentración de iones de hidrógeno, para calcular el pH y así poder clasificar las sustancia
    
'''

#import
import math 
from math import *

#ph
h = float(input("Ingrese la concentración de iones de hidrógeno: "))

#Ecuación
ph = math.log(h) * (-1)

#Condicionales
if ph < 7:
    print(f"El valor del pH es", ph, "y se encuentra en condición Ácida")
if ph == 7:
    print(f"El valor del pH es", ph, "y se encuentra en condición Neutra")
if ph > 7:
    print(f"El valor del pH es", ph, "y se encuentra en condición Alcalina")
if ph == 14:
    print(f"El valor del pH es 1y se encuentra en condición Ácida")

