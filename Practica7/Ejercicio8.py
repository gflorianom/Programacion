"""Biel Floriano Morey - 1� DAW - PRACTICA7 - EJERCICIO 8
Escribe un programa que pida una frase, y pase la frase como par�metro a una funci�n que debe
eliminar los espacios en blanco (compactar la frase). El programa principal imprimir� por pantalla
el resultado final. 
"""
print "Escribe una frase"
f=raw_input()

def frase(f):
    valor=''
    for i in range(len(f)):
        if f[i] == ' ':
            valor+=(f[i].replace(' ', ''))
        else:
            valor+=f[i]
    return valor
print frase(f)
