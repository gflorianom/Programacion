"""Biel Floriano Morey - 1� DAW - PRACTICA4 - EJERCICIO 5
Escriu un programa que demani l'amplada i al�ada d'un rectangle i ho dibuixi de la seg�ent
manera:"""
print "Dime el ancho que tiene el rectangulo"
ancho=input()
print "Dime la altura que tiene el rectangulo"
altura=input()
for i in range(0, ancho):
    for j in range(0, altura):
        print "*",
    print " "
