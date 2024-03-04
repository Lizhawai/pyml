#!/usr/bin/env python3

def add_matrices2D(arr1, arr2):
    add_arr = []
    m = len(arr1)
    a = len(arr2)
    n = len(arr1[0])
    b = len(arr2[0])

    if m == a and n == b:
        for i in range(m):
            col = [0] * n
            add_arr.append(col)


        for i in range(m):
            for j in range(n):
                add_arr[i][j] = arr1[i][j] + arr2[i][j]
        return add_arr
    else:
        return None

if __name__ == '__main__':
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
   