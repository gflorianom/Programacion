"""Biel Floriano Morey - 1� DAW - PRACTICA5 - EJERCICIO 7
Escriu un programa que demani un nombre (l�mit) i despr�s et demani nombres fins a qu� la suma
dels nombres introduits superi un nombre inicial. El programa termina escribint la llista de
nombres. 

"""
print "Escribe el n�mero l�mite"
n=int(raw_input())
print "Escribe un valor"
m=int(raw_input())
n2=m
valores=[m]
while n>n2:
    print "Introduce otro valor"
    m=int(raw_input())
    n2=m+n2
    valores.append(m)

print "El l�mite a superar es " ,n, ". La lista creada �s" ,valores
