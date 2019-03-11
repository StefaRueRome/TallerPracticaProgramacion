annio=int(input("Ingrese un año a evaluar: "))
if annio%4==0:
	if annio%100==0:
		if annio%400==0:
			print("El año es bisiesto")
		else:
			print("El año no es bisiesto")
	else:
		print("El año es bisiesto")
else:
	print("El año no es bisiesto")