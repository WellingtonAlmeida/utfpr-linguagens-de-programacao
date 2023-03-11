# -*- coding: utf-8 -*-

value = int(input())

print(value)

banknotes = (100, 50, 20, 10, 5, 2, 1)
amount = value

for banknote in banknotes:
    number_of_banknotes = int(amount / banknote)
    print(f"{number_of_banknotes} nota(s) de R${banknote},00")
    amount = amount % banknote
