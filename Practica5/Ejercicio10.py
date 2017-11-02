"""Biel Floriano Morey - 1º DAW - PRACTICA5 - EJERCICIO 10
Escriu un programa que et demani els noms i notes d'alumnes. Si escrius una nota fora de
l'interval de 0 a 10, el programa entendrà que no vols introduir més notes d'aquest alumne. Si no
escrius el nom, el programa entendrà que no vols introduir més alumnes. Nota: La llista en la que
es guarden els noms i notes és [ [nom1, nota1, nota2, etc], [nom2, nota1, nota2, etc], [nom3,
nota1, nota2, etc], etc] 
 
"""
print "Dame un nombre"
n=raw_input()
personas=[]
personas2=[]
while n<>"":
    personas.append(n)
    print "Escribe una nota"
    nota=float(input())
    while nota<=10 and nota>=0:
        personas.append(nota)
        print "Escribe otra nota"
        nota=float(input())
    personas2.append(personas)
    print "Introduce otro nombre"
    n=raw_input()
    personas=[]
print "Las notas de los alumnos son: "
print (personas2)
