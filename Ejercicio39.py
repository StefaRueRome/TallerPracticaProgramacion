import math
a=int(input("Introduzca el valor de A: "))
b=int(input("Introduzca el valor de B: "))
c=int(input("Introduzca el valor de C: "))
x=(b**2)-(4*a*c)
if x<0:
	print("La solución de la ecuación solo es posible en números complejos")
else:
	if x>0:
		x1=-b+(math.sqrt(x))/(2*a)
		x2=-b-(math.sqrt(x))/(2*a)
		print("La solución para la parte positiva es: ",x1,"Y para la parte negativa es: ",x2)