print "Escribe una cantidad (entera) y te diré cuantas gruesas, docenas y unidades són"
n=input()
g=n/144
r=n%144
d=r/12
u=r%12
print n, "son" ,g, "gruesas," ,d, "docenas y" ,u, "unidades"
