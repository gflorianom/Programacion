"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 3
Escriu un programa que demani notes i les guardi en una llista. Per a terminar d'introduir notes,
escriu una nota que no estigui entre 0 i 10. El programa termina escrivint la llista de notes. 
"""
print "Escribe una nota"
n=float(raw_input())
notas=[]

while (n<=10 and n>=0):
    notas.append(float(n))    
    n=float(raw_input("otra nota"))

print notas
