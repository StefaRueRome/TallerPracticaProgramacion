num1=int(input("ingrese el primer número: "))
num2=int(input("ingrese el segundo número: "))
num3=int(input("ingrese el tercer número: "))
suma=num1+num2
if suma>num3:
	print("La suma de los dos primeros números es mayor que: ",num3)
else:
	if suma<num3:
		print("La suma de los dos primeros números es menor que: ",num3)
