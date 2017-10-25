"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 9
Escriu un programa que demani l'amplada i l'alçada d'un rectangle i ho dibuixi de la següent
manera:
"""
print "Dime el ancho que tiene el rectangulo"
ancho=input()
print "Dime la altura que tiene el rectangulo"
altura=input()
for i in range(altura):
    if i==0 or i==altura-1:
       for j in range(ancho-1):
           print "*",
    else:
        for k in range(ancho-1):
            if k==0 or k==ancho-1:
                print"*",
            else:
                print" ",
    print "*", "\n",
