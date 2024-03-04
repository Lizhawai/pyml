#!/usr/bin/env python3

def cat_arrays(arr1, arr2):
    new_list = arr1[:]
    m = len(arr2)

    for i in range(m):
        new_list.append(arr2[i])

    return new_list

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))
    print(arr1)
    print(arr2)