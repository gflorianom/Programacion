"""BIEL FLORIANO MOREY - 1ºDAW- PRÁCTICA 7- EJERCICIO 7
Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento.
El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla. """
def meter_frase():
    frase=raw_input("dime una frase: ")
    return frase
       
def contar_a(texto):
    vocales=['a']
    contador=0
    for i in texto:
        if i in vocales:
            contador+=1
    return contador

def contar_e(texto):
    vocales=['e']
    contador=0
    for i in texto:
        if i in vocales:
            contador+=1
    return contador

def contar_i(texto):
    vocales=['i']
    contador=0
    for i in texto:
        if i in vocales:
            contador+=1
    return contador

def contar_o(texto):
    vocales=['o']
    contador=0
    for i in texto:
        if i in vocales:
            contador+=1
    return contador

def contar_u(texto):
    vocales=['u']
    contador=0
    for i in texto:
        if i in vocales:
            contador+=1
    return contador

def resultado(a,e,i,o,u):
    print "En tu frase hay" ,a, "a"
    print "En tu frase hay" ,e, "e"
    print "En tu frase hay" ,i, "i"
    print "En tu frase hay" ,o, "o"
    print "En tu frase hay" ,u, "u"

a = meter_frase()
b = contar_a(a)
c = contar_e(a)
d = contar_i(a)
e = contar_o(a)
f = contar_u(a)
total = resultado(b,c,d,e,f)
