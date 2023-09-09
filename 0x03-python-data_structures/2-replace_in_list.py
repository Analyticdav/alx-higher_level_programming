#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    list_length = len(my_list)

    if (idx < 0 or idx > list_length):

        return (None)

    else:

        return (my_list[idx])
