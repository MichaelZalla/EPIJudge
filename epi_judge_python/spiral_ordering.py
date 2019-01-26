from typing import List

from test_framework import generic_test

import math, itertools

def spiral_boundary(M, n, level):

    if n == 1:

        return [M[0][0]]

    if n % 2 == 1 and level == math.floor(n / 2):

        value = M[level][level]

        return [value]

    low_bound, high_bound = level, n-level-1

    top = list(M[low_bound][i] for i in range(low_bound, high_bound+1))
    bottom = list(M[high_bound][i] for i in reversed(range(low_bound, high_bound+1)))
    right = list(M[i][high_bound] for i in range(low_bound, high_bound+1))
    left = list(M[i][low_bound] for i in reversed(range(low_bound, high_bound+1)))

    return top + right[1:-1] + bottom + left[1:-1]

def matrix_in_spiral_order(M: List[List[int]]) -> List[int]:

    n = len(M)
    levels = math.ceil(n/2)

    return list(itertools.chain.from_iterable([spiral_boundary(M, n, level) for level in range(levels)]))

# Mn1 = [0]

# print(spiral_boundary(Mn1, 1, 0))

# Mn2 = [[5,7],[2,9]]

# print(spiral_boundary(Mn2, 2, 0))

# Mn3 = [[5,7,3],[2,9,0],[9,6,2]]

# print(spiral_boundary(Mn3, 3, 0))
# print(spiral_boundary(Mn3, 3, 1))

# Mn4 = [[5,7,3,2],[2,9,0,5],[9,6,2,9],[6,3,7,1]]

# print(spiral_boundary(Mn4, 4, 0))
# print(spiral_boundary(Mn4, 4, 1))

# Mn5 = [[8,2,7,5,8],[5,3,2,9,8],[1,2,5,9,2],[9,8,1,2,5],[7,2,6,4,1]]

# print(spiral_boundary(Mn5, 5, 0))
# print(spiral_boundary(Mn5, 5, 1))
# print(spiral_boundary(Mn5, 5, 2))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering.py",
                                       "spiral_ordering.tsv",
                                       matrix_in_spiral_order))
