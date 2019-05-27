from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:

    # Tracks the largest unplaced elements of A and B

    b_end = n - 1
    a_end = m - 1

    # Defines a 'hole' that we've move values into

    i = m + n - 1

    while a_end > -1 and b_end > -1:

        # Takes max values from both arrays (unnecessary)

        # if A[a_end] == B[b_end]:
        #     A[i] = A[a_end]
        #     A[i-1] = B[b_end]
        #     a_end, b_end = a_end - 1, b_end - 1
        #     i -= 1

        # Takes max value from A

        if A[a_end] > B[b_end]:
            A[i] = A[a_end]
            a_end -= 1

        # Takes max value from B

        else:
            A[i] = B[b_end]
            b_end -= 1

        i -= 1

    # Takes any remaining members of B

    while b_end > -1:
        A[i] = B[b_end]
        i, b_end = i - 1, b_end - 1

# A1 = [2,3,4,None]
# B1 = [1]

# A2 = [5,13,17,None,None,None,None,None]
# B2 = [3,7,11,19]

# A3 = [None,None,None,None,None,None]
# B3 = [-5,-3,-1,-1,3,6]

# merge_two_sorted_arrays(A1, 3, B1, 1)

# print(A1)

# merge_two_sorted_arrays(A2, 3, B2, 4)

# print(A2)

# merge_two_sorted_arrays(A3, 0, B3, 6)

# print(A3)

# exit()

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
