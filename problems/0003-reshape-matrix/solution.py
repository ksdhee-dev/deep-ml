import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    flat = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            flat.append(a[i][j])
    
    element_count = len(flat)
    m = new_shape[0]
    n = new_shape[1]

    reshaped_matrix = []
    if element_count == m*n:
        for j in range(m):
            row = []
            for i in range(n):
                row.append(flat[j * n+i])
            reshaped_matrix.append(row)
    
    return reshaped_matrix