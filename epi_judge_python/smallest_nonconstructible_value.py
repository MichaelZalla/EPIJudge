from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value_naive(nums: List[int]) -> int:

    if not nums:
        return 1

    subset_sums = [0] * 2**len(nums)

    constructible = [False] * (1 + sum(nums) + 1)

    for index, num in enumerate(nums):

        for prev_subsets_index in range(2**index):

            subset_sum = subset_sums[prev_subsets_index] + num

            subset_sums[2**index + prev_subsets_index] = subset_sum

            constructible[subset_sum] = True

    index = 1

    while constructible[index]:
        index += 1

    return index

def smallest_nonconstructible_value(nums: List[int]) -> int:

    lcv = 0

    for num in sorted(nums):
        if num > lcv + 1:
            break
        lcv += num

    return lcv + 1


# print(smallest_nonconstructible_value([]))
# print(smallest_nonconstructible_value([1]))
# print(smallest_nonconstructible_value([50]))
# print(smallest_nonconstructible_value([1,1,1,1,5,10,20,50]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
