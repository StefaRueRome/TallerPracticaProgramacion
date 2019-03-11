num1=int(input("ingrese el primer número: "))
num2=int(input("ingrese el segundo número: "))
num3=int(input("ingrese el tercer número: "))
if num1>num2 and num1>num3:
	print("El número mayor es: ",num1)
else:
	if num2>num1 and num2>num3:
		print("El número mayor es: ",num2)
	else:
		if num3>num1 and num3>num2:
			print("El número mayor es: ",num3)
		
			

if num1<num2 and num1<num3:
	print("El número menor es: ",num1)
else:
	if num2<num1 and num2<num3:
		print("El número menor es: ",num2)
	else:
		if num3<num1 and num3<num2:
			print("El número menor es: ",num3)
