"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 3
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos
palabras y sustituya la primera por la segunda en la lista. 
"""
print "Cuantas palabras quieres introducir?"
p=int(raw_input())
palabras=[]
encontradas=0
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print palabras
print "Que palabra quieres sustituir?"
sustituir=raw_input()
print "por la palabra"
remplazar=raw_input()
for j in range(len(palabras)):
    if (str(sustituir) == str(palabras[j])):
        palabras[j]=str(remplazar)
print palabras
