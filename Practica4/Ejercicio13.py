"""Biel Floriano Morey - 1º DAW - PRACTICA4 - EJERCICIO 13
Escriu un programa que imprimeixi les taules de multiplicar del 0 al 9."""
for i in range(0, 10):
    print "Tabla del " + str(i)
    print "-----------"
    for j in range(0, 11):
        print str(i) + " x " + str(j) + " = " + str(i*j)

    print "\n"
