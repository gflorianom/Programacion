"""Biel Floriano Morey - 1� DAW - PRACTICA6 - EJERCICIO 10
Escribe un programa que pida un n�mero y a continuaci�n escriba la lista de todos los divisores
del n�mero (incluidos el uno y �l mismo).   
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

