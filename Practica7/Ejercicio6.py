"""BIEL FLORIANO MOREY - 1ºDAW- PRÁCTICA 7- EJERCICIO 6
Escribe un programa que lea el nombre de una persona y un carácter,
le pase estos datos a una función que comprobará  si dicho carácter está en su nombre.
El resultado de dicha función lo imprimirá el programa principal por pantalla. """
def meter_nombre():
    nombre=raw_input("dime un nombre: ")
    return nombre
def meter_letra():
    letra=raw_input("dime una letra: ")
    return letra
def comprobar_letra(palabra, letra):
    flag=False
    if letra in palabra:
        flag=True
    return flag
def resultado(esta):
    if esta==True:
        print "La letra SI que está en el nombre"
    else:
        print "La letra NO está en el nombre"
    
    
        
a = meter_nombre()
b = meter_letra()
comprobar = comprobar_letra(a, b)
resultado(comprobar)
