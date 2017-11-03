"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 10
Escribe un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo).   
"""
print("Inserta un numero para saber sus divisores:")
n=int(input())
divisores=[]
contador=0

for i in range (1, n+1):
    if n % i == 0:
        divisores.append(i)
        i = i+1
        contador += 1

print n, " tiene " ,contador, " divisores: " ,divisores

