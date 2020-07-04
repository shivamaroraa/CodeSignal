import numpy as np


def sudoku(grid):
    a = np.array(grid)

    for i in range(0, 3):
        for j in range(0, 3):
            if len(set(list(a[i*3:(i*3)+3, j*3:(j*3)+3].flatten()))) != 9:
                return False
                
    for i in range(0, 9):
        if len(set(list(a[:, i]))) != 9 or len(set(list(a[i, :]))) != 9:
            return False
            
    return True