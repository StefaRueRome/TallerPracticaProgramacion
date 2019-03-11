import math
print("Programa para calcular el área de un hexágono")
lado=float(input("Ingrese la longitud del lado: "))
perimetro=lado*6
area=(3*math.sqrt(3)*lado**2)/2
print("El área es: ", area ,"centímetros cuadrados")