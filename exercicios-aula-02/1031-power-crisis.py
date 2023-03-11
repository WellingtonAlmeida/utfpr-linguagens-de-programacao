# -*- coding: utf-8 -*-

n = int(input())
cities = list(range(1, n+1))
first_city = 1
last_city = 13

for m in cities:
    random_list = []
    current_city = first_city
    for city in cities:
        if current_city > n:
            current_city = current_city - n
        random_list.append(current_city)
        current_city = current_city + m
    if random_list[-1] == last_city:
        print(random_list)
        print(m)
        break