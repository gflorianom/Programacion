"""Biel Floriano Morey - 1� DAW - PRACTICA7 - EJERCICIO 4
Escribe un programa que pida una frase, y le pase como par�metro a una funci�n dicha frase. La
funci�n debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla. 
  
"""
print "Escribe una frase"
f=raw_input()

def frase(f):
    valor=''
    for i in range(len(f)):
        if f[i] == ' ':
            valor+='*'
        else:
            valor+=f[i]
    return valor
print frase(f)

