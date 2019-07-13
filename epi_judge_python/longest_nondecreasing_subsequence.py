from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:

    longest_ending_at_index = [1] * len(A)

    for i in range(1, len(A)):

        longest_below_value = 0

        for j in range(0, i):

            if A[j] <= A[i]:

                longest_below_value = max(
                    longest_below_value,
                    longest_ending_at_index[j]
                )

        longest_ending_at_index[i] = longest_below_value + 1

    return max(longest_ending_at_index)

def longest_nondecreasing_subsequence_length_pythonic(A: List[int]) -> int:

    longest_ending_at_index = [1] * len(A)

    for i in range(1, len(A)):

        longest_ending_at_index[i] = 1 + max(
            (longest_ending_at_index[j] for j in range(i) if A[i] >= A[j]),
            default=0
        )

    return max(longest_ending_at_index)


# print(longest_nondecreasing_subsequence_length([0,8,4,12,2,10,6,14,1,9]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
