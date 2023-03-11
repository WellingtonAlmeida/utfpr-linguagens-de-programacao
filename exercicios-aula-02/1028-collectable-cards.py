# -*- coding: utf-8 -*-

import math

number_of_tests = int(input())

for i in range(number_of_tests):
    cards = input().split()
    richard_cards, vicent_cards = [int(card) for card in cards]
    print(math.gcd(richard_cards, vicent_cards))
