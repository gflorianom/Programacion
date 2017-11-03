"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 1
Escriu un programa que te demani paraules i les guardi en una llista. Per a terminar d'introduir
paraules, simplement pitja Enter. El programa termina escribint la llista de paraules.  
"""
print "Cuantas palabras quieres introducir?"
p=int(raw_input())
palabras=[]

for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print palabras
