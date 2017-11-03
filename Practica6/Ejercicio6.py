"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 6
Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear
una lista distinta).  

"""
print "Cuantas palabras quieres introducir?"
p=int(raw_input())
palabras=[]
palabras2=palabras
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print palabras
print palabras2[::-1]
