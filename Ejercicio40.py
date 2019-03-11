usuario_1=input("Ingrese el nombre del usuario: ")
contrasenna_1=input("Ingrese una contraseña: ")
usuario="estefany"
contrasenna=12345
if usuario_1==usuario and contrasenna_1!=contrasenna:
	print("La contraseña es incorrecta")
else:
	if usuario_1!=usuario and contrasenna_1==contrasenna:
		print("El usuario es incorrecto")
	else:
		if usuario_1!=usuario and contrasenna_1!=contrasenna:
			print("El usuario y la contraseña son incorrectos")
		else:
			if usuario_1==usuario and contrasenna_1==contrasenna:
				print("El usuario y la contraseña son correctos")



	



	
