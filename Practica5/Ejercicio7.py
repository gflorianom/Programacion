"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 7
Escriu un programa que demani un nombre (límit) i després et demani nombres fins a què la suma
dels nombres introduits superi un nombre inicial. El programa termina escribint la llista de
nombres. 

"""
print "Escribe el número límite"
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

print "El límite a superar es " ,n, ". La lista creada és" ,valores
