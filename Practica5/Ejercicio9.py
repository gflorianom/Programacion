"""Biel Floriano Morey - 1� DAW - PRACTICA5 - EJERCICIO 9
Escriu un programa que et demani noms de persones i els seus n�meros de tel�fon. Per a
terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
termina escribint noms i n�meros de tel�fon. Nota: La llista en la que es guarden els noms i
n�meros de tel�fon �s [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc] 
 
"""
print "Dame un nombre"
n=str(raw_input())
personas=[]
personas2=[]
while n<>"":
    personas.append(n)
    print "Dame el telefono"
    t=str(raw_input())
    personas.append(t)
    personas2.append(personas)
    print "Dame un nombre"
    n=str(raw_input())
    personas=[]
print (personas2)

