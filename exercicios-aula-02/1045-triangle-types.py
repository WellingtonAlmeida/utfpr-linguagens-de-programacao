# -*- coding: utf-8 -*-

numbers = input().split()
numbers = [float(number) for number in numbers]
numbers.sort()
a, b, c = numbers

if c >= (a+b):
    print("NAO FORMA TRIANGULO")
else:
    square_hypotenuse = c**2
    square_other_sides_sum = a**2 + b**2

    if square_hypotenuse == square_other_sides_sum:
        print("TRIANGULO RETANGULO")
    elif square_hypotenuse > square_other_sides_sum:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
