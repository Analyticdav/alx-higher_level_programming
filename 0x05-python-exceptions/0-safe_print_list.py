#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elements in range(0, x):
            print(my_list[elements], end='')
        print('')
        return(x)
    except:
        print('')
        return(elements)
