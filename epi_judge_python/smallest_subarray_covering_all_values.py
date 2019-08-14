import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(C: List[str], T: List[str]) -> Subarray:

    min_distance, min_subarray = len(C), Subarray(start=0, end=len(C)-1)

    indices = { token: [-1] * (len(C) - 1) + [len(C) - 1 if C[-1] == token else -1 ] for token in T }

    for i in reversed(range(len(C) - 1)):
        for token in T:
            indices[token][i] = i if C[i] == token else indices[token][i+1]

    for start in set(indices[T[0]]):

        token_index, end = 1, start

        while end != -1 and token_index < len(T):
            token = T[token_index]
            end = indices[token][end]
            token_index += 1

        if end != -1:
            distance = end - start + 1
            if distance < min_distance:
                min_distance, min_subarray = distance, Subarray(start=start,end=end)

    return min_subarray


# print(find_smallest_sequentially_covering_subset(['A','B','C','A','B','A','A'], ['B','C','A']))
# print(find_smallest_sequentially_covering_subset(['S','O','B'], ['S','O','B']))

# exit()


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
