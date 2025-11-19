import math
angle = float(input("angulo: "))
epsilon = float(input("epsilon: "))
L = float(input("longitud: "))
vel = float(input("velocidad: "))

phi = math.radians(270 - angle)
phip = math.radians(angle -90)

A = (L*(math.cos(phip) - 1), L*math.sin(phip))
B = (L*(math.cos(phi) + 1), L*(math.sin(phi)))
Ae = (L*(math.cos(phip) - 1), L*(math.sin(phip) + epsilon))
Be = (L*(math.cos(phi) + 1), L*(math.sin(phi) + epsilon))

print("B: "+str(B))
print("A: "+str(A))
print("B epsilon: "+str(Be))
print("A espilon: "+str(Ae))

pritn("el numero de reynolds es: "+str(1*vel*1/1))