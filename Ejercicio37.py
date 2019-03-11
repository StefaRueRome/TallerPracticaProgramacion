distancia=int(input("Ingrese el número de kilómetros a recorrer: "))
precio_distan=int(distancia*5000)
estancia=int(input("Ingrese el número de días de estancia: "))
percio_estan=int(estancia*100000)
valor_pasaje=precio_distan+percio_estan
precio_total=int(valor_pasaje*0.15)
if distancia>1000 and estancia>7:
	print("El valor del pasaje con un 5% de descuento es de: ",precio_total)
else:
	print("El valor del pasaje es de: ", valor_pasaje)
