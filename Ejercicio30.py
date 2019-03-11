venta=int(input("Ingrese el valor de la venta: "))
valor_iva=int(venta*0.19)
venta_iva=venta+valor_iva
desc=int(venta_iva*0.05)
descu_total=venta-desc

if venta>150000:
	print("La venta es mayor a 150.000 por lo tanto tiene un descuento del 5%, el valor total de la venta es: ",descu_total)
else:
	print("El valor del total de la venta es: ",venta_iva)





