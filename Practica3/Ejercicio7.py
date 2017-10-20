print "Introduce un número de segundos y te diré cuuantas horas y cuantosminutos són"
s=input()
h=s/3600
r=s%3600
m=r/60
o=r%60
print s, "segundos son" ,h, "horas" ,m, "minutos y" ,o, "segundos"
