"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 8
Escriu un programa que et demani primer un nombre i després et demani nombres fins a què la
suma dels nombres introduïts coincideixi amb el nombre inicial. El programa termina escribint la
llista de nombres. 
"""
print "Escribe el número límite"
n=int(raw_input())
print "Escribe un valor"
m=int(raw_input())

while m>n:
    print "El numero " ,m, "es demasiado grande, escribe otro numero entero:"
    m=int(raw_input())

suma=m
valores=[m]

while suma<n:
    print "Introduce otro valor"
    m=int(raw_input())
    while suma + m > n:
        print "El numero " ,m, "es demasiado grande, introduzca otro"
        m=int(raw_input())
    suma += m
    valores += []
    valores.append(m)
print "El límite a superar es " ,n, ". La lista creada és" ,valores
