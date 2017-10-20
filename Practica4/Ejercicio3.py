"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 3
Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""
print "Introduce un número"
n=input()
print "Introduce un segundo número mayor que el primero"
m=input()
for i in range(n, m+1):
    i=sum(range(n, m+1))
    print "La suma desde " ,n, "hasta" ,m, "és: " ,i
