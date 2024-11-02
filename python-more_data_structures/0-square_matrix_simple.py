#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for temp_one in matrix:
        temp_matrix = list()
        for temp_two in temp_one:
            temp_matrix.append(temp_two**2)
        new_matrix.append(temp_matrix)
    return new_matrix
