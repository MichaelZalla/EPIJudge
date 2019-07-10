from typing import List

import random
import functools

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_subset_recursive(n: int, k: int) -> List[int]:

    def random_subset_helper(k: int):

        if k == 0:
            return k_subset

        value = -1

        while value in D:
            value = random.randrange(0, n + 1)

        k_subset.append(value)

        D[value] = True

        return random_subset_helper(k-1)

    k_subset, D = [], { -1: True }

    return random_subset_helper(k)


def random_subset_list(n: int, k: int) -> List[int]:

    unchosen, chosen = [digit for digit in range(n)], []

    for _ in range(k):

        random_index = random.randrange(0, len(unchosen))

        chosen.append(unchosen[random_index])

        unchosen.pop(random_index)

    return chosen


def random_subset_subdivide(n: int, k: int) -> List[int]:

    if k == 0:
        return []

    subset, boundaries = [], [-1, n + 1]

    for _ in range(k):

        candidates = []

        # In this iteration, produce (len(boundaries) - 1) random candidates;
        # one will be chosen at random to further subdivide our boundary space;

        for j in range(0, len(boundaries) - 1):

            left, right = boundaries[j], boundaries[j+1]

            # Check that left and right are not contiguous (i.e., space)

            if right - left > 1:

                candidate = random.randrange(left+1, right)

                candidates.append(candidate)

        random_candidate_index = random.randrange(0, len(candidates))

        random_candidate = candidates[random_candidate_index]

        # Add the randomly chosen candidate to our subset

        subset.append(random_candidate)

        # Move the new boundary into its sorted position in boundaries

        boundaries.append(random_candidate)

        j = len(boundaries) - 1

        while j and boundaries[j-1] > boundaries[j]:
            boundaries[j-1], boundaries[j] = boundaries[j], boundaries[j-1]
            j -= 1

    return subset


def random_subset_hasharray(n: int, k: int) -> List[int]:

    modified = {}

    for i in range(k):

        chosen_index = random.randrange(i, n)

        chosen_index_mapped = modified.get(chosen_index, chosen_index)

        ith_index_mapped = modified.get(i, i)

        modified[chosen_index_mapped] = ith_index_mapped
        modified[ith_index_mapped] = chosen_index_mapped

    return [modified[i] for i in range(k)]


# print(random_subset_hasharray(10,0))
# print(random_subset_hasharray(10,1))
# print(random_subset_hasharray(10,2))
# print(random_subset_hasharray(10,3))
# print(random_subset_hasharray(10,10))
# print(random_subset_hasharray(100,50))

# exit()


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset_hasharray(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
