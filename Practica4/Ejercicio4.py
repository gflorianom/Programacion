"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 4
Escriu un programa que demani un nombre i calculi el seu factorial."""
print "Introduce un número y te diré su factorial"
n=input()
factorial=1
for i in range(1, n+1):
    factorial=factorial*i
    print "El factorial de " ,n, "es: " ,factorial,
