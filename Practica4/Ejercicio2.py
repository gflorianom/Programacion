"""Biel Floriano Morey - 1� DAW - PRACTICA4 - EJERCICIO 2
Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins s�n
senars (=�impares�) des del primer fins al segon."""
print "Escribe un n�mero"
n=input()
print "Escribe un segundo n�mero mayor que el anterior"
m=input()
for i in range(n, m+1):
    if i%2==0:
        print "El n�mero" ,i, "es par"
    else:
        print "El n�mero" ,i, "es impar"
