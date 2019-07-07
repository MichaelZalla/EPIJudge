from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:

    # Build a lookup table for all unique integers in A

    D, max_interval = {}, 0

    for value in A:
        D[value] = value

    # Iterate over the entries in D, considering each integer value as though it
    # were the final integer in some interval in A (i.e., largest integer in the
    # interval);

    # List allows us to modify the set of keys in D during our pass;

    for key in list(D.keys()):

        # We may have deleted this key during our pass

        if not key in D:
            continue

        # Can we 'connect' our integer to the interval ending with its
        # predecessor (i.e., value - 1)?

        next = D[key] - 1

        while next in D:

            # Merges the two intervals, deleting 'next' from our table;

            D[key] = D[next]

            del D[next]

            next = D[key] - 1

        # Check if this value's current interval is the largest we've seen;

        interval = key - D[key] + 1

        if interval > max_interval:
            max_interval = interval

    return max_interval


# print(longest_contained_range([3,-2,7,9,8,1,2,0,-1,5,8]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
