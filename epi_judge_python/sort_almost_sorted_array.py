from typing import Iterator, List

from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:

    result, heap, seq_iter = [], [], iter(sequence)

    for _ in range(k):
        next_elem = next(seq_iter, None)
        if next_elem is not None:
            heapq.heappush(heap, next_elem)

    while heap:

        next_elem = next(seq_iter, None)

        if next_elem is not None:
            result.append(heapq.heappushpop(heap, next_elem))
        else:
            result.append(heapq.heappop(heap))

    return result

# k, S = 2, [0,3,2,1,5,4,6,9,7,8]

# # k, S = 2, [0,3,2]

# print(sort_approximately_sorted_array(S, k))

# exit()


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
