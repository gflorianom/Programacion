"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 9
Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista con las palabras de la primera, pero sin palabras repetidas (el orden de las palabras
en la segunda lista no es importante).  
"""
print "Cuantas palabras tiene la primera lista?"
p=int(raw_input())
palabras = []
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print "La lista creada es:", palabras
for i in range(len(palabras)-1, -1, -1):
    if palabras[i] in palabras[:i]:
        del(palabras[i])
print "La lista sin repeticiones es:", palabras
