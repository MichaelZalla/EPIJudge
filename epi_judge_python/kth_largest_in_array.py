from typing import List

from test_framework import generic_test

import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.

def find_kth_largest(k: int, A: List[int]) -> int:

    def partition_around_pivot(A, left, right, pivot_index):

        pivot_elem = A[pivot_index]

        new_pivot_index = left

        A[pivot_index], A[right] = A[right], A[pivot_index]

        # Swap smaller elements with pivot_index until pivot is sorted

        for i in range(left, right):

            if A[i] < A[right]:
                A[i], A[new_pivot_index] = A[new_pivot_index], A[i]
                new_pivot_index += 1

        A[new_pivot_index], A[right] = A[right], A[new_pivot_index]

        return new_pivot_index

    left, right, target_index = 0, len(A) - 1, len(A) - k

    while True:

        new_pivot_index = partition_around_pivot(A, left, right, random.randint(left, right))

        if new_pivot_index < target_index:
            left = new_pivot_index + 1

        elif new_pivot_index > target_index:
            right = new_pivot_index - 1

        else:
            return A[new_pivot_index]

# B = [0]
# C = [1,5]
# D = [11,8,7,6,1,9,10,5,4,3,12,2,0]
# E = [6,19,13,10,2,4,15,20,8,17,18,1,12,14,5,11,7,16,0,9,3]

# # print(B, find_kth_largest(1, B))
# # print(C, find_kth_largest(1, C))
# # print(D, find_kth_largest(4, D))
# print(E, find_kth_largest(4, E))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
