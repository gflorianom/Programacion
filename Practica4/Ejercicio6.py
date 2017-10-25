"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 6
Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:"""
print "Dime la altura del triangulo"
a=input()
for i in range(1, a+1):
    for j in range(i):
        print "*",
    print " "
