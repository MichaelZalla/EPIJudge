from typing import Iterator, List

from test_framework import generic_test

import math
import heapq

def get_online_median(sequence: Iterator[int]) -> List[float]:

    result, min_heap, max_heap = [], [], []

    for value in sequence:

        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, value))

        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) == len(max_heap):
            result.append((min_heap[0] + (-max_heap[0])) * 0.5)
        else:
            result.append(min_heap[0])

    return result

# S = []
# S = [0]
# S = [0,1]
# S = [0,1,0,3]
# S = [0,2,2,3,1,0,5,4,7]

# get_online_median(S)

# exit()

def online_median_wrapper(sequence):
    return get_online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
