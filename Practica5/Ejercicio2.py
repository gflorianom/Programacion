"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 2
Escriu un programa que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres.  
"""
print "Escribe una número"
n=raw_input()
numeros=[]

while n<>"":
    numeros.append(int(n))    
    n=raw_input("Escribe más números")

print numeros
