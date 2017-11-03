"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 2
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista. 
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
print "Que palabra quieres contar las veces hay en las lista?"
buscar=raw_input()
for j in range(len(palabras)):
    if (str(buscar) == str(palabras[j])):
        encontradas+=1
print "La palabra" ,buscar, " aparece " ,str(encontradas), "veces"
