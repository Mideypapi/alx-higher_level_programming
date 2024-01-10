#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [x[:] for x in matrix]
    for n in range(len(new_matrix)):
        for m in range(len(new_matrix[n])):
            new_matrix[n][m] = (new_matrix[n][m]) ** 2
    return (new_matrix)
