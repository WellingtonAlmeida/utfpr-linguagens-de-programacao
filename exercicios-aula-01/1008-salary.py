# -*- coding: utf-8 -*-

employee_number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

salary = worked_hours * amount_per_hour

print("NUMBER = {:d}".format(employee_number))
print("SALARY = U$ {:.2f}".format(salary))
