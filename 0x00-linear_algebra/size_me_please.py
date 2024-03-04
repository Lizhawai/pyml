#!/usr/bin/env/python3
# You can also use a while loop
# But with recursion, you have to use 
size = []
def matrix_shape(matrix):

    if type(matrix) != type(5):
        size.append(len(matrix))
        return matrix_shape(matrix[0])
    return size

size = []