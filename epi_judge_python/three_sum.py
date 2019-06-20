from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:

    def has_two_sum(left, right, sum):

        while left <= right:
            if A[left] + A[right] == sum:
                return True
            elif A[left] + A[right] < sum:
                left += 1
            else:
                right -= 1

        return False

    A.sort()

    for index in range(0, len(A)):

        if has_two_sum(index, len(A) - 1, t - A[index]):
            return True

    return False


# print(has_three_sum([0], 0))
# print(has_three_sum([1,2,3], 3))
# print(has_three_sum([1,2,3], 4))
# print(has_three_sum([1,2,3], 5))
# print(has_three_sum([1,2,3], 6))
# print(has_three_sum([], 21))
# print(has_three_sum([2,3,5,7,11], 21))
# print(has_three_sum([2,3,5,7,11], 22))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
