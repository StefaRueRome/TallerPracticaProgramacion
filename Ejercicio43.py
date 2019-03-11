num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))
if num2>num1 and num3>num2:
	print("Los números están incrementando")
else:
	if num2<num1 and num3<num2:
		print("Los números están disminuyendo")
	else:
		print("Los números no están incrementando ni disminuyendo")