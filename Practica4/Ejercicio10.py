"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 10
Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
"""
print "Dame la altura de la piramide"
a=input()
for i in range(a):
    espacios=a-i-1
    asteriscos=1+i*2
    print " "*espacios+"*"*asteriscos
