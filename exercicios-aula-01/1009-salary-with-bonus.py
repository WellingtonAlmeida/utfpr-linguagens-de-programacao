# -*- coding: utf-8 -*-

seller_name = input()
fixed_salary = float(input())
total_value_sold = float(input())

sales_commission = 0.15

total = fixed_salary + (total_value_sold * sales_commission)

print("TOTAL = R$ {:.2f}".format(total))
