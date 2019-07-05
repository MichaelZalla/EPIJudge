from test_framework import generic_test

import math


def square_root(n: float) -> float:

    left, right = (1.0, n) if n > 1 else (n, 1.0)

    while not math.isclose(left, right):

        mid = 0.5 * (left + right)

        squared = mid * mid

        if squared < n:
            left = mid
        else:
            right = mid

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
