#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    list_length = len(my_list) - 1

    if (idx < 0 or idx > list_length):

        return (my_list)

    else:

        copy_of_list = my_list[:]

        copy_of_list[idx] = element

        return (copy_of_list)
