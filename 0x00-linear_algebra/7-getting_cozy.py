#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    new_matrix = []
    print(new_matrix)
    if axis == 0:
        new_matrix = mat1[:]
        new_matrix.extend(mat2)
        return new_matrix
    
    else:
        new_matrix = mat1[:]
        for i in range(len(mat1)):
            new_matrix[i].append(mat2[i][0])
        return new_matrix
    
if __name__ == '__main__':
    mata = [[1, 2], [3, 4]]
    matb = [[5, 6]]
    matc = [[7], [8]]
    mat4 = cat_matrices2D(mata, matb)
    mat5 = cat_matrices2D(mata, matc, axis=1)
    print(mat4)
    print(mat5)
    # mat1[0] = [9, 10]
    # mat1[1].append(5)
    # print(mat1)
    # print(mat4)
    # print(mat5)
