"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 4
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista 
"""
print "Cuantas palabras quieres introducir?"
p=int(raw_input())
palabras=[]
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print palabras
print "Que palabra quieres borrar?"
borrar=raw_input()
while borrar in palabras:
    palabras.remove(borrar)
print palabras
