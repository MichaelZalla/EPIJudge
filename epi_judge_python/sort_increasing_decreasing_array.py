from typing import List
import heapq

from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:

    def merge_sorted_arrays(arrays):

        return list(heapq.merge(*arrays))

    arrays_to_merge, increasing = [], True

    start = 0

    for i in range(start + 1, len(A) + 1):

        if i == len(A) or \
            (A[i-1] >= A[i] and increasing) or \
            (A[i-1] < A[i] and not increasing):

            arrays_to_merge.append(A[start:i] if increasing else A[i-1:start-1:-1])

            start = i

            increasing = not increasing

    return merge_sorted_arrays(arrays_to_merge)


# print(sort_k_increasing_decreasing_array([]))
# print(sort_k_increasing_decreasing_array([0]))
# print(sort_k_increasing_decreasing_array([0,1,2]))
# print(sort_k_increasing_decreasing_array([0,-1,-2]))
# print(sort_k_increasing_decreasing_array([0,0,0,0,0,0,0,0]))
# print(sort_k_increasing_decreasing_array([0,1,0,1,0,1,0,1]))
# print(sort_k_increasing_decreasing_array([0,1,2,3,4,5,6,7,8,9]))
# print(sort_k_increasing_decreasing_array([9,8,7,6,5,4,3,2,1,0]))
# print(sort_k_increasing_decreasing_array([1,3,5,4,2,0,2,4,6,7,5,3]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
