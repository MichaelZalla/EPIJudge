import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def num_unique_elems(A):

    unique, prev_seen = 0, 0

    for i in range(len(A)):

        if i == 0 or A[i] != prev_seen:

            prev_seen = A[i]

            unique += 1

    return unique

def delete_duplicates(A: List[int]) -> int:

    last_unique_index = 0
    next_unique_index = last_unique_index + 1

    while next_unique_index < len(A):

        # Advance next_unique_index until we encounter an element E that is
        # > A[last_unique_index], or until we reach the last valid index in A

        while next_unique_index < len(A) - 1 and A[next_unique_index] <= A[last_unique_index]:
            next_unique_index += 1

        # Check case where next_unique_index is the last valid index in A

        if A[next_unique_index] == A[last_unique_index]:
            next_unique_index += 1
            continue

        # At this point, next_unique_index points to next instance of any unseen
        # element in A; move it to the end of our sublist of unique elements

        A[last_unique_index + 1], A[next_unique_index] = A[next_unique_index], A[last_unique_index + 1]

        # Increase the size of our unique sublist by 1

        last_unique_index += 1
        next_unique_index += 1

    # Number of unique elements will be (last_unique_index + 1)

    return last_unique_index + 1

def delete_duplicates_fast(A):

    # Points to the next available slot in our sublist of unique elements

    next_unique_index = 1

    # Index 1 is our first unvisited element in A

    for i in range(1, len(A)):

        last_unique_index = next_unique_index - 1

        # Compare this element to our last-seen unique element

        if A[last_unique_index] != A[i]:

            # Write this element to the next available slot in our sublist

            A[next_unique_index] = A[i]

            next_unique_index += 1

    return next_unique_index

def remove_key_stable(A, key):

    for i in range(len(A)):

        # Locate the next instance of key

        if A[i] == key:

            # If it's at the end, we're done

            if i == len(A) - 1:
                continue

            # Otherwise, find the next instance of not-key

            j = i + 1

            while j < len(A) and A[j] == key:
                j += 1

            # Couldn't locate another not-key in A

            if j == len(A):
                continue

            # Swap this key with the not-key instance

            A[i], A[j] = A[j], A[i]

    return

# remove_key_stable([9,1,4,6,7,4,2,1,4,8,6,4], 4)

# exit()

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
