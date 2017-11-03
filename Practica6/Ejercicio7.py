"""Biel Floriano Morey - 1º DAW - PRACTICA6 - EJERCICIO 7
Escribe un programa que permita crear dos listas de palabras y que, a continuación, escriba las
siguientes listas (en las que no debe haber repeticiones):
• Lista de palabras que aparecen en las dos listas
• Lista de palabras que aparecen en la primera lista, pero no en la segunda
• Lista de palabras que aparecen en la segunda lista, pero no en la primera
• Lista de palabras que aparecen en ambas listas   

"""
print "Cuantas palabras tiene la primera lista?"
p=int(raw_input())
palabras=[]
palabras2=[]
for i in range(p):
    print "Introduce la palabra: "
    pa=raw_input()
    palabras.append(pa)
print "La primera lista es: " ,palabras
print "Cuantas palabras tiene la segunda lista?"
p2=int(raw_input())
for j in range(p2):
    print "Introduce la palabra: "
    pa2=raw_input()
    palabras2.append(pa2)
print "La segunda lista es: " ,palabras2
comunes = []
for i in palabras:
    if i in palabras2:
         comunes += [i]
print "Palabras que aparecen en las dos listas:", comunes
soloPrimera = []
for i in palabras:
    if i not in palabras2:
        soloPrimera += [i]
print "Palabras que sólo aparecen en la primera lista:", soloPrimera
soloSegunda = []
for i in palabras2:
    if i not in palabras:
        soloSegunda += [i]
print "Palabras que sólo aparecen en la segunda lista:", soloSegunda
todaspalabras = comunes + soloPrimera + soloSegunda
print "Todas las palabras:", todaspalabras
