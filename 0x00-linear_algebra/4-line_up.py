#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    a = len(arr1)
    b = len(arr2)

    sum_arr = []
    if a == b:
        for i in range(a):
            sum_arr.append(arr1[i] + arr2[i])
        return sum_arr
    return
    
if __name__ == '__main__':
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    add_arrays(arr1, arr2)
    print(arr1)
    print(arr2)
    add_arrays(arr1, [1, 2, 3])