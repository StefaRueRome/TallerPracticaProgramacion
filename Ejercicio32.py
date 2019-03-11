n1=float(input("Ingrese la primera nota: "))
nota1=n1*0.15
n2=float(input("Ingrese la segunda nota: "))
nota2=n2*0.20
n3=float(input("Ingrese la tercer nota: "))
nota3=n3*0.15
n4=float(input("Ingrese la cuarta nota: "))
nota4=n4*0.30
n5=float(input("Ingrese la quinta nota: "))
nota5=n5*0.20
nota_final=(nota1+nota2+nota3+nota4+nota5)
if nota_final<2.0:
	print("No puede habilitar, su nota es: ",nota_final)
else:
	if nota_final<3.0:
		print("Reprobó, su nota es: ",nota_final)
	else:
		if nota_final>4.5:
			print("Felicitaciones es un excelante estudiante, su nota es: ",nota_final)
		else:
			if nota_final>=3.0:
				print("Aprobó, su nota es: ",nota_final)
