"""Biel Floriano Morey - 1º DAW - PRACTICA7 - EJERCICIO 3
Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste
debe mostrar la frase con un carácter en cada línea.  
"""
print "Escribe una frase"
frase=raw_input()
for i in range(0, len(frase)):
    print frase[i]

