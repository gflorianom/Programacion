"""Biel Floriano Morey - 1� DAW - PRACTICA7 - EJERCICIO 3
Escribe un programa que lea una frase, y la pase como par�metro a un procedimiento, y �ste
debe mostrar la frase con un car�cter en cada l�nea.  
"""
print "Escribe una frase"
frase=raw_input()
for i in range(0, len(frase)):
    print frase[i]

