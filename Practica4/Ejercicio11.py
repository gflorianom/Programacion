"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 11
Escriu un programa que demani un nombre i retorni els seus divisors."""
print("Inserta un numero para saber sus divisores:")

n=int(input())
divisores=[]

for i in range (1, n+1):
    if n % i == 0:
        divisores.append(i)
        i = i+1
        
print("Los divisores de " + str(n) + " son " + str(divisores)[1:-1] + ".")
