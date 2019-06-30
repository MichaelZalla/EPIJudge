from typing import List

from test_framework import generic_test


def get_max_trapped_water(S: List[int]) -> int:

    i, j, running_max_capacity = 0, len(S) - 1, 0

    while i < j:

        height = min(S[i], S[j])

        capacity = height * (j-i)

        if capacity > running_max_capacity:
            running_max_capacity = capacity

        # Move in, looking for a higher-capacity pair

        while i < j and S[i] <= height:
            i += 1

        while i < j and S[j] <= height:
            j -= 1

    return running_max_capacity

# print(get_max_trapped_water([1,2]))
# print(get_max_trapped_water([2,1]))
# print(get_max_trapped_water([1,2,3]))
# print(get_max_trapped_water([3,2,1]))
# print(get_max_trapped_water([1,2,2,1]))
# print(get_max_trapped_water([1,2,2,2,1]))
# print(get_max_trapped_water([1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
