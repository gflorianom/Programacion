"""Biel Floriano Morey - 1� DAW - PRACTICA7 - EJERCICIO 2
Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes), los pase como par�metros a una funci�n, y �sta debe unirlos y devolver
una �nica cadena. La cadena final la imprimir� el programa por pantalla. 
"""
print "Dime tu nombre"
nombre=raw_input()
print "Dime tu primer apellido"
apellido1=raw_input()
print "Dame tu segundo apellido"
apellido2=raw_input()

nombrecompleto= nombre + ' ' + apellido1 + ' ' + apellido2
print "Tu nombre y apellidos completo es: "
print nombrecompleto


