"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 8
Escribe un programa que permita crear una lista de palabras y que, a continuación, ordene la lista
por orden alfabético.  
"""
print "Cuantas palabras tiene la lista?"
p=int(raw_input())
palabras=[]
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
    palabras2=sorted(palabras)
print "La primera lista es: " ,palabras
print "La lista ordenada es: " ,palabras2

