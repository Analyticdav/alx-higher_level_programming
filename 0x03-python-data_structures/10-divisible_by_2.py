#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):

    multiples = []

    for integers in range(len(my_list)):

        if my_list[integers] % 2 == 0:

            multiples.append(True)

        else:

            multiples.append(False)
