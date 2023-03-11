# -*- coding: utf-8 -*-

a = float(input())
b = float(input())

a_weight = 3.5
b_weight = 7.5

total_weight = a_weight + b_weight

media = ((a * a_weight) + (b * b_weight)) / total_weight

print("MEDIA = {:.5f}".format(media))
