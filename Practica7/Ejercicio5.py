"""Biel Floriano Morey - 1� DAW - PRACTICA7 - EJERCICIO 5
Escribe un programa que te pida una frase y una vocal, y pase estos datos como par�metro a una
funci�n que se encargar� de cambiar todas las vocales de la frase por la vocal seleccionada.
Devolver� la funci�n la frase modificada, y el programa principal la imprimir�: 
"""
print "Introduce una frase: "
f= raw_input()
print "Introduce una vocal: "
vocal= raw_input()
vocales= ['a','e','i','o','u']
def frase(f,vocal):
    result=""
    for i in range(len(f)):
        if f[i] in vocales:
            result+=vocal
        else:
           result+=f[i]
    return result
print frase(f,vocal)


