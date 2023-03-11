# -*- coding: utf-8 -*-

def read_values():
    values = input().split()
    return [float(value) for value in values]


x1, y1, x2, y2 = read_values()

while not(x1 == y1 == x2 == y2 == 0):
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or abs(x2-x1) == abs(y2-y1):
        print(1)
    else:
        print(2)
    x1, y1, x2, y2 = read_values()
