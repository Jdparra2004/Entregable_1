# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:07:17 2023

@author: Valentina Galindo y Juan David Parra
"""

#librerias 
import numpy as np
from numpy import sqrt

#variables y matrices

n = int(input("Ingrese el número de filas que tendrá la matriz: "))
a = n

M = np.random.randint(9, size=(n,a))

#n es fila y a es columna 
#lista 

sumatoria_columnas = []
sumatoria_filas = []
sumatoria_frobenius = []

#definir funcion para filas
#norma 1 
print("\n---para las columnas---")     
#FILA ES N
#COLUMNA A 
def columna(a):
    suma=0
    
    for i in range(0,a):
        x = M[i,:]
        suma = abs(suma + x)
        normac = suma
        
        sumatoria_columnas.append(i)
        
        #retorno
        
    return normac

print("\nlos valores de la norma 1 de las columna son respectivamente es:",columna(a))

maxcolumna = np.max(columna(a))
print("el valor de las normas 1 de las columna es:", maxcolumna)
#ABAJO 
#norma Infinita
print("\n---para las filas---")
def fila(n):
    suma = 0
    
    for j in range(0,n):
        x = M[:,j]
        suma = abs(suma+x)
        normaf = suma
        
        sumatoria_filas.append(j)
        
        #retorno
        
    return normaf

print("\nlos valores de la norma infinito de las filas son respectivamente es:",fila(n))

maxfila = np.max(fila(n))
print("el valor de las norma infinito de las filas es:", maxfila)

#definir nroma de frobenius
print("\n---norma de frobenius---")
def normfrobenius():
        suma=0
        
        for i in range(0,a):
            for j in range(0,n):
                x = M[i,j]
                suma=(suma+x**2)
                sumatoria_columnas.append(i)
                normfrobenius = sqrt(suma)
            
            #retorno
            
        return normfrobenius
print("\nel valor de la norma de frobenius:",normfrobenius())
    
#comparacion con metodo linalg
normafrob2 = np.linalg.norm(M)
print("El valor de la norma matriz por el metodo de linalg de numpy es:", normafrob2)

