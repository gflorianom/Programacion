print "Introduce un n�mero de segundos y te dir� cuuantas horas y cuantosminutos s�n"
s=input()
h=s/3600
r=s%3600
m=r/60
o=r%60
print s, "segundos son" ,h, "horas" ,m, "minutos y" ,o, "segundos"
