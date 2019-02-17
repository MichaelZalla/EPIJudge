from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sequences: List[List[int]]) -> List[int]:

    result, heaps = [], []

    # Cleans up empty sequences

    sequences = [seq for seq in sequences if seq]

    # Construct a min-heap for each sequence in the input

    for i in range(len(sequences)):
        heap = sequences[i]
        heapq.heapify(heap)
        heaps.append(heap)

    # While there are still non-empty heaps remaining

    while heaps:

        min_index = 0

        # Locate the heap with the smallest min element

        for i in range(1, len(heaps)):
            if heaps[i][0] < heaps[min_index][0]:
                min_index = i

        result.append(heapq.heappop(heaps[min_index]))

        if not heaps[min_index]:
            del heaps[min_index]

    return result

def merge_sorted_arrays_const_space(sequences: List[List[int]]) -> List[int]:

    # NOTE(mzalla) We need explicit None checks, as sequence keys might be falsy
    # (i.e., zero)

    result, min_heap = [], []

    # Initialize iterators for each sequence in our input

    seq_iterators = [iter(seq) for seq in sequences]

    # Build a k-size heap from the min elem of each of our k input sequences;
    # the heap will store tuples containing an element (value) and the index of
    # the sequence from which it came;

    for index, iterator in enumerate(seq_iterators):

        first_elem = next(iterator, None)

        if first_elem is not None:
            heapq.heappush(min_heap, (first_elem, index))

    while min_heap:

        # Determine the current min element (and its associated sequence)

        min_elem, min_index = heapq.heappop(min_heap)

        min_iterator = seq_iterators[min_index]

        # Adds the current min elem to our result

        result.append(min_elem)

        # Advances the min iterator, returning next elem (if possible)

        next_elem = next(min_iterator, None)

        # Adds next elem from that sequence to our heap (if possible)

        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, min_index))

    return result

# S1 = [1,7,8,2,9,8,3,7,4,6,8]
# S2 = [1,2,0,3,3,8,9,0,2,0,9]
# S3 = [2,1,0,8,9,2,3,1,2,7,3]
# S4 = [7,3,8,2,5,1,0,1,0,0,2]

# S = [S1, S2, S3, S4]

# # S = [[],[],[]]

# for i in range(len(S)):
#     S[i].sort()

# print(merge_sorted_arrays_const_space(S))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays_const_space))
