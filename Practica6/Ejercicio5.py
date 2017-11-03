"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 5
Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la
primera lista los nombres de la segunda lista. 

"""
print "Cuantas palabras quieres introducir?"
p=int(raw_input())
palabras=[]
borradas=[]
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print palabras
print "Cuantas palabras quieres eliminar?"
eliminar=int(raw_input())
for j in range(eliminar):
    print "Introduce la palabra: "
    palabra=raw_input()
    palabras.remove(palabra)
    borradas.append(palabra)
print "Las palabras a eliminar son: " ,borradas
print "La lista ahora es: " ,palabras

