"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 2
Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins són
senars (=”impares”) des del primer fins al segon."""
print "Escribe un número"
n=input()
print "Escribe un segundo número mayor que el anterior"
m=input()
for i in range(n, m+1):
    if i%2==0:
        print "El número" ,i, "es par"
    else:
        print "El número" ,i, "es impar"
