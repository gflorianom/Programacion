"""Biel Floriano Morey - 1� DAW - PRACTICA5 - EJERCICIO 6
Escriu un programa que demani primer dos nombres (m�xim i m�nim) i que despr�s te demani 2
nombres situats entre ells. Per a terminar d'escriure nombres, escriu un nombre que no sigui
compr�s entre els dos valors inicials. El programa termina escribint la llista de nombres.  
"""
print "Escribe un numero"
n=int(raw_input())
print "Escribe un numero major que" ,n,": "
m=int(raw_input())
numeros=[]
while m<=n:
    print m, " no �s major que " ,n, "vuelve a intentarlo"
    m=int(raw_input())
print "Escribe un numero entre " ,n, " y " ,m
a=int(raw_input())
while (a<m and a>n):
    numeros.append(a)
    print "Escribe otro numero entre" ,n, " y " ,m
    a=int(raw_input())

print "Los numeros situados entre " ,n, " y " ,m, " son " ,numeros

