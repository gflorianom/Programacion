"""Biel Floriano Morey - 1� DAW - PRACTICA4 - EJERCICIO 3
Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""
print "Introduce un n�mero"
n=input()
print "Introduce un segundo n�mero mayor que el primero"
m=input()
for i in range(n, m+1):
    i=sum(range(n, m+1))
    print "La suma desde " ,n, "hasta" ,m, "�s: " ,i
