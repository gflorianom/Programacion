"""Biel Floriano Morey - 1� DAW - PRACTICA4 - EJERCICIO 7
Escriu un programa que demani l'al�ada d'un triangle i ho dibuixi de la seg�ent manera:"""
print "Dime la altura del triangulo"
a=input()
for i in range(a, 0, -1):
    for j in range(i):
        print "*",
    print " "
