#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10

    b = 5

    """ Addition of a and b """

    print("{} + {} = {}".format(a, b, add(a, b)))

    """subtraction of a and b """

    print("{} - {} = {}".format(a, b, sub(a, b)))

    """Multiplication of a and b """

    print("{} * {} = {}".format(a, b, mul(a, b)))
    
    """Division of a and b """

    print("{} / {} = {}".format(a, b, div(a, b)))
