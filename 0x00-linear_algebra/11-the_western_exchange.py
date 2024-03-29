#!/usr/bin/env python3
import numpy as np

def np_transpose(matrix):
    return matrix.T

mat1 = np.array([1, 2, 3, 4, 5, 6])
mat2 = np.array([])
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
[[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
# print(np_transpose(mat1))
# print(mat1)
# print(np_transpose(mat2))
# print(mat2)
print(np_transpose(mat3).shape)
print(mat3.shape)