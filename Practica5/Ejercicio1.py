"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 1
Escriu un programa que te demani paraules i les guardi en una llista. Per a terminar d'introduir
paraules, simplement pitja Enter. El programa termina escribint la llista de paraules. 
"""
print "Escribe una palabra"
p=raw_input()
palabras=[]

while p<>"":
    palabras.append(p)    
    p=raw_input("Escribe más palabras")

print palabras

