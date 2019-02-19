from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:

    lower, upper = 0, len(A)-1

    while lower < upper:

        mid = lower+(upper-lower)//2

        if A[mid] < A[upper]:
            upper = mid
        else:
            lower = mid+1


    return lower

# A1 = []
# A2 = [3]
# A3 = [3,1]
# A4 = [3,5,6,0,2]
# A5 = [3,4,5,6,7,0,1,2]
# A6 = [0,1,2,3,4,5,6,7]

# print(search_smallest(A1))
# print(search_smallest(A2))
# print(search_smallest(A3))
# print(search_smallest(A4))
# print(search_smallest(A5))
# print(search_smallest(A6))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
