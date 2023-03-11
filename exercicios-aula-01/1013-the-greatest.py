# -*- coding: utf-8 -*-

def greatest(a, b):
    return int((a+b+abs(a-b))/2)
    
values = input().split()

values = [int(value) for value in values]

the_greatest = greatest(values[0], greatest(values[1], values[2]))

print("{} eh o maior".format(the_greatest))
