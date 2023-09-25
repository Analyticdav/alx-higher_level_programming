#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    value = 0
    for items in range(list_length):
        try:
            value = (my_list_1[items] / my_list_2[items])
        except ZeroDivisionError:
            print('division by 0 is not allowed')
        except TypeError:
            print('You have a wrong type')
        except IndexError:
            print('your input is out of range')
        finally:
            new_list.append(value)
    return(new_list)
