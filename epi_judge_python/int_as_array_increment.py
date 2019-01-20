from typing import List

from test_framework import generic_test

def plus_one(A: List[int]) -> List[int]:

    index = len(A) - 1

    while index > -1 and A[index] == 9:

        A[index] = 0
        index -= 1

    if index == -1:
        A.insert(0, 1)

    else:
        A[index] += 1

    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
