"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 5
Escriu un programa que te demani dos nombres cada vegada més grans i els guardi en una llista.
Per a terminar d'escriure els nombres, escriu un nombre que no sigui major a l'anterior. El
programa termina escribint la llista de nombres. 
"""
print "Escribe un numero"
n=int(raw_input())
print "Escribe un numero major que: " ,n
m=int(raw_input())
numeros=[n]
while m>n:
    n=m
    numeros.append(n)
    print "Escribe un numero major que: " ,n
    m=int(raw_input())

print "Los numeros introducidos son " ,numeros
