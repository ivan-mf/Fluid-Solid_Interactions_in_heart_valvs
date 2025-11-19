import math
angle = float(input("angulo: "))
epsilon = float(input("epsilon: "))

phi = math.radians(270 - angle)
phip = math.radians(angle -90)

A = (math.cos(phip) - 1, math.sin(phip))
B = (math.cos(phi) + 1, math.sin(phi))
Ae = (math.cos(phip) - 1, math.sin(phip) + epsilon)
Be = (math.cos(phi) + 1, math.sin(phi) + epsilon)

print("B: "+str(B))
print("A: "+str(A))
print("B epsilon: "+str(Be))
print("A espilon: "+str(Ae))

