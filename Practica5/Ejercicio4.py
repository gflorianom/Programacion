"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 4
Escriu un programa que te demani dos nombres, de manera que el segon sigui major que el
primer. El programa termina escrivint els dos nombre tal i com es demana. 
"""
print "Escribe un numero"
n=int(raw_input())
print "Escribe un numero major que" ,n,": "
m=int(raw_input())
while m<=n:
    print m, " no és major que " ,n, "vuelve a escribir un numero"
    m=int(raw_input())
    
print "Los dos numeros que has escrito son: " ,n, " y " ,m
