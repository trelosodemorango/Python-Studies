import math
print("Solucionador de Equações do Segundo Grau")
print("Escreva o a:")
a = int(input())
print("Escreva o b:")
b = int(input())
print("Escreva o c:")
c = int(input())

print(str(a) + "x² " + str(b) + "x " + str(c))
delta = (b**2)-4*a*c
print("Resultado:")
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)
print("x1: " + str(x1))
print("x2: " + str(x2))

