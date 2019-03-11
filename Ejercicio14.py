import math
print("Programa para calcular el tiempo de caída de un objeto")
h=float(input("Introduce la altura: "))
t=(2*h)/9.81
tiempo=math.sqrt(t)
print("El tiempo de caída es de", t,"segundos")