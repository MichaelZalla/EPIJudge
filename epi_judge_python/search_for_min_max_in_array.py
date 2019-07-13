import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max_increasing_decreasing(A: List[int]) -> MinMax:

    if not A:
        return MinMax(None, None)

    min, max, decreasing = A[0], A[0], True

    cmp_count = 0

    for i in range(1, len(A)):

        cmp_count += 1

        did_decrease = A[i] < A[i-1]

        if decreasing and not did_decrease:

            cmp_count += 2

            if A[i-1] < min:
                min = A[i-1]

            if A[i] > max:
                max = A[i]

            decreasing = False

        elif not decreasing and did_decrease:

            cmp_count += 2

            if A[i-1] > max:
                max = A[i-1]

            if A[i] < min:
                min = A[i]

            decreasing = True

    cmp_count += 1
    cmp_count += 1

    if decreasing and A[-1] < min:
        min = A[-1]

    elif not decreasing and A[-1] > max:
        max = A[-1]

    print('n=', len(A), '2(n-1)=', 2*(len(A)-1), 'cmp_count=', cmp_count)

    return MinMax(min, max)


cmp_count = 0

def find_min_max_paired_candidates(A: List[int]) -> MinMax:

    def min_max(a, b):

        global cmp_count

        cmp_count += 1

        return MinMax(a, b) if a < b else MinMax(b, a)

    if len(A) <= 1:
        return MinMax(A[0], A[0])

    global_min_max = min_max(A[0], A[1])

    for i in range(2, len(A) - 1, 2):

        local_min_max = min_max(A[i], A[i+1])

        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )

    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )

    print('n=', len(A), '2(n-1)=', 2*(len(A)-1), 'cmp_count=', cmp_count)

    return global_min_max


# print(find_min_max_paired_candidates([3]))
# print(find_min_max_paired_candidates([1,2,3,4,5]))
# print(find_min_max_paired_candidates([5,4,3,2,1]))
# print(find_min_max_paired_candidates([1,2,3,3,2,1]))
# print(find_min_max_paired_candidates([3,2,1,1,2,3]))
# print(find_min_max_paired_candidates([1,2,1,2,1,2]))
# print(find_min_max_paired_candidates([3,2,5,1,2,4]))

# exit()


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max_paired_candidates,
                                       res_printer=res_printer))
