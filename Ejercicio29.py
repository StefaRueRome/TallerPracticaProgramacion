num=int(input("Ingrese un número: "))
if num%2==0 and num>0:
	print("El número es par positivo")

if num%2==0 and num<0:
	print("El número es par negativo")

else:
	if num%2!=0 and num<0:
		print("El número es impar negativo")
	
	if num%2!=0 and num>0:
		print("El número es par positivo")
 