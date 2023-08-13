'''
Prueba de escritorio, revisión del codigo
'''
import time

n = float(input("Ingrese el valor de 'n' : "))

i = 1

while (i <= n):
    p = 0
    j = 0
    while (j < i):
        p = p+ (2 * j + 1)
        j = j + 1
    print(p)
    i = i + 1
    time.sleep(1)

