# -*- coding: utf-8 -*-

n = int(input())

while n > 0:

    done = False
    m = 1

    while done == False:

        cities = list(range(1, n+1))
        pointer = 0
        last_city = 13
        random_list = []

        while len(cities) > 0:

            current_city = cities[pointer]
            cities.remove(current_city)
            random_list.append(current_city)
            if len(cities) > 0:
                pointer = (pointer + m - 1) % len(cities)

        if len(random_list) == n and random_list[-1] == last_city:
            done = True
            print(m)

        m = m+1

    n = int(input())
