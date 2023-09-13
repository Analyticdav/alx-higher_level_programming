#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[q ** 2 for q in p] for p in matrix]
    return (new_matrix)
