"""Biel Floriano Morey - 1� DAW - PRACTICA5 - EJERCICIO 2
Escriu un programa que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres.  
"""
print "Escribe una n�mero"
n=raw_input()
numeros=[]

while n<>"":
    numeros.append(int(n))    
    n=raw_input("Escribe m�s n�meros")

print numeros
