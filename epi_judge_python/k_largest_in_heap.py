from typing import List
import heapq

from test_framework import generic_test, test_utils


class HeapItem:

    def __init__(self, heap, index):
        self.heap = heap
        self.index = index

    def __lt__(self, other):
        return self.heap[self.index] >= self.heap[other.index]

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:

    if not A or not k:
        return []

    k_largest, max_heap = [], [HeapItem(A, 0)]

    while len(k_largest) < k and max_heap:

        max_index = heapq.heappop(max_heap).index
        max_value = A[max_index]

        k_largest.append(max_value)

        left_child_index = max_index * 2 + 1
        right_child_index = left_child_index + 1

        if left_child_index < len(A):
            heapq.heappush(max_heap, HeapItem(A, left_child_index))
            if right_child_index < len(A):
                heapq.heappush(max_heap, HeapItem(A, right_child_index))

    return k_largest


# print(k_largest_in_binary_heap([], 0))
# print(k_largest_in_binary_heap([], 3))
# print(k_largest_in_binary_heap([2,1], 0))
# print(k_largest_in_binary_heap([2,1], 3))
# print(k_largest_in_binary_heap([3,2,1], 3))
# print(k_largest_in_binary_heap([5,4,1,3,2], 3))
# print(k_largest_in_binary_heap([561,314,401,28,156,359,271], 4))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
