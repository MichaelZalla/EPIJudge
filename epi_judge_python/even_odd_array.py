import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def get_first_odd(A, start):

    for i in range(start, len(A)):
        if A[i] %2 == 1:
            return i

    return len(A)

def get_last_even(A, end):

    for i in range(end-1, -1, -1):
        if A[i] % 2 == 0:
            return i

    return -1

def even_odd_double_scan(A):

    first_odd = get_first_odd(A, 0)
    last_even = get_last_even(A, len(A))

    while first_odd < last_even:

        temp = A[last_even]
        A[last_even] = A[first_odd]
        A[first_odd] = temp

        first_odd = get_first_odd(A, first_odd + 1)
        last_even = get_last_even(A, last_even - 1)

    return A

def even_odd(A: List[int]) -> None:

    next_even = 0
    next_odd = len(A) - 1

    while next_even < next_odd:

        if A[next_even] % 2 == 0:

            next_even += 1

        else:

            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part (element=" + str(a) + ")")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
