# -*- coding: utf-8 -*-

values = input().split()
a = float(values[0])
b = float(values[1])
c = float(values[2])

pi = 3.14159

triangle_rectangle_area = a*c/2
circle_area = pi*(c**2)
trapezium_area = (a+b)*c/2
square_area = b**2
rectangle_area = a*b

print("TRIANGULO: {:.3f}".format(triangle_rectangle_area))
print("CIRCULO: {:.3f}".format(circle_area))
print("TRAPEZIO: {:.3f}".format(trapezium_area))
print("QUADRADO: {:.3f}".format(square_area))
print("RETANGULO: {:.3f}".format(rectangle_area))
