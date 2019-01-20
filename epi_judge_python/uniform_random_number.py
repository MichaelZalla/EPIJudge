import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

def zero_one_random():
    return random.randrange(2)

def uniform_random_binary_search(lower_bound: int, upper_bound: int) -> int:

    left = lower_bound
    right = upper_bound + 1

    # Performs a random binary 'search'

    while left < right:

        # Computes the middle index between left and right for this iteration

        mid = (left + right) // 2 #math.ceil((right - left) // 2)

        # Determine in which direction our 'search' will proceed

        if zero_one_random():

            # Continue by 'searching' the right half

            left = mid #+ 1
            # right -= 1

        else:

            # Continue by 'searching' the left half

            # left += 1
            right = mid #- 1

    result = left

    # print(result)

    return result

def uniform_random_concatenate(lower_bound, upper_bound):

    # Computes the range of possible return values

    range = upper_bound - lower_bound + 1

    # Until we find a sufficient result

    while True:

        result, bit_index = 0, 0

        # For each significant binary digit in 'range'

        while (1 << bit_index) < range:

            # OR a new random bit into result and increment our bit index

            result = (result << 1) | zero_one_random()

            bit_index += 1

        # Tests whether result (offset from lower_bound) fits within the range

        if result < range:

            break

    # Returns lower_bound plus our random offset

    return lower_bound + result


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random_binary_search(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
