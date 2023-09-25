#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    x_values = 0
    try:
        for items in range(0, x):
            if isinstance(my_list[items], int):
                print("{:d}".format(my_list[items]), end='')
                x_values = x_values + 1
        print()
        return(x_values)
    except TypeError:
        print()
