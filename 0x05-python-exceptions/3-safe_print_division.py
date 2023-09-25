#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divisiion = a / b
    except:
        division = None
    finally:
        print("The division is: {}".format(division))
        return(division)
