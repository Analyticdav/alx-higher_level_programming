#!/usr/bin/python3
""" This returns the number of lines of a text file """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, encoding='utf-8') as p:
        lines = 0
        for line in p:
            lines += 1
        return lines
