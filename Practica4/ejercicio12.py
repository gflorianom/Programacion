"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 12
Escriu un programa que demani un nombre i escrigui si és primer o no.
"""
print("Inserta un numero para saber sus divisores:")

n=int(input())
divisores=[]

for i in range (1, n+1):
    if n % i == 0:
        divisores.append(i)
        i = i+1
        if len(divisores) > 2: 
            print "El numero" ,n, "no es primo."
            break
        elif i > n:
            print "El numero" ,n, "es primo."
        else:
            continue
