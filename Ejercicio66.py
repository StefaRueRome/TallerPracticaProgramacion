num=int(input("Ingrese un número entero positivo: "))
while num<0:
	print("El número no es válido, vuelva a intentarlo")
	num=int(input("Ingrese un número: "))
	if num>0:
		print(num)