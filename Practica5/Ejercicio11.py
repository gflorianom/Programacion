"""Biel Floriano Morey - 1� DAW - PRACTICA5 - EJERCICIO 11
Escriu un programa per a jugar a endivinar un nombre (l'ordinador �pensa� el nombre i l'usuari l'ha
d'endevinar). El programa comen�a demanant entre qu� nombres est� el nombre a endevinar,
s'�inventa� un nombre a l'atzar i despr�s l'usuari va probant valors i el programa va decidint si s�n
massa grans o petits. Pista:  
"""
import random

intentos = 0

print "Introduce valor m�nimo"
minim=int(raw_input())

print "Introduce valor m�ximo"
maxim=int(raw_input())

x = random.randint (minim, maxim)

while intentos < 6:
    intentos = intentos + 1
    print "Elige un numero del " ,minim, "al" ,maxim
    numero = raw_input()
    numero = int (numero)
    if numero < x:
        print ("Tu numero es mas bajo")
    if numero > x:
        print ("Tu numero es mas alto")
    if numero == x:
        break

if numero == x:
    print ("Eres un genio....")
    print (nombre + " lo lograste con %d intentos" % (intentos))
    print ("Nos vemos....")
    
if numero != x:
    print ("Has perdido, sera en otra oportunidad...")
    print ("Nos vemos")
