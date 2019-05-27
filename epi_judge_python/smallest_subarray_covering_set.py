import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

import itertools
import math

def each_overlaps_naive(indices, sorted_indices_subarray):

    for entry in indices.values():
        if(not set(entry).intersection(set(sorted_indices_subarray))):
            return False

    return True

def find_smallest_subarray_covering_set_naivet(words: List[str],
                                        keywords: Set[str]) -> Subarray:

    if(not len(words)):
        raise ValueError('Document is empty!')

    if(not len(keywords)):
        raise ValueError('No keywords specified!')

    indices = {}

    for k in keywords:
        indices[k] = []

    # Records index of each instance of each keyword in corpus

    for i in range(0, len(words)):
        if words[i] in keywords:
            indices[words[i]].append(i)

    # Creates a sorted list of all recorded indices

    sorted_indices = sorted(list(itertools.chain.from_iterable(list(indices.values()))))

    # Begin with the smallest window size and grow the window during our search

    for window_size in range(len(keywords), len(words) + 1):

        costs, min_cost, min_start = {}, math.inf, -1

        # Check each subarray of size window_size in our list of sorted_indices

        for start in range(0, len(words) - window_size + 1):

            sorted_indices_subarray = sorted_indices[start : start + window_size]

            if each_overlaps_naive(indices, sorted_indices_subarray):

                cost = sorted_indices[start+window_size-1] - sorted_indices[start]

                if cost < min_cost:
                    min_start, min_cost = start, cost

        # Did we find the minimum-cost subarray?

        if min_start != -1:
            return Subarray(sorted_indices[min_start], sorted_indices[min_start + window_size - 1])

    # Keywords are not entirely contained in 'words'

    raise ValueError('Keywords "{0}" not in text "{1}"'.format(keywords, words))

def find_smallest_subarray_covering_set_ON2(words, keywords):

    min_cost, result = math.inf, Subarray(-1, -1)

    for start in range(0, len(words) - len(keywords) + 1):

        unvisited, end = {}, start

        for keyword in keywords:
            unvisited[keyword] = True

        while end < len(words):

            word = words[end]

            if word in unvisited:
                del unvisited[word]

            if not unvisited:
                cost = end - start + 1
                if cost < min_cost:
                    min_cost, result = cost, Subarray(start, end)

            end += 1

    return result

def find_smallest_subarray_covering_set_ON(words, keywords):

    keywords_remaining, uncovered_count = collections.Counter(keywords), len(keywords)

    result = Subarray(-1, -1)

    left = 0

    # Begin by incrementing our end index

    for right, word in enumerate(words):

        if word in keywords:

            # Update counts for this keyword

            keywords_remaining[word] -= 1

            if keywords_remaining[word] >= 0:
                uncovered_count -= 1

        # If we cover all keywords between left and right

        while uncovered_count == 0:

            # If current min cost is infinite, or if new cost is smaller

            if result == Subarray(-1, -1) or right - left < result[1] - result[0]:

                result = Subarray(left, right)

            word = words[left]

            if word in keywords:

                # We've 're-covering' this keyword as we move left towards right
                keywords_remaining[word] += 1

                if keywords_remaining[word] > 0:
                    uncovered_count += 1

            left += 1

    return result

# print('a:: ', find_smallest_subarray_covering_set(['a'], []))
# print(':a: ', find_smallest_subarray_covering_set([], ['a']))

# print('a:a: ', find_smallest_subarray_covering_set(['a'], ['a']))
# print('a,b:a: ', find_smallest_subarray_covering_set(['a','b'], ['a']))
# print('b,a:a: ', find_smallest_subarray_covering_set(['b','a'], ['a']))
# print('b,a:b: ', find_smallest_subarray_covering_set(['b','a'], ['b']))
# print('a,b:a,b: ', find_smallest_subarray_covering_set(['a','b'], ['a','b']))
# print('b,a:a,b: ', find_smallest_subarray_covering_set(['b','a'], ['a','b']))
# print('a,a,b,d,c,b,a,d,c,c,a:a,c,d: ', find_smallest_subarray_covering_set(['a','a','b','d','c','b','a','d','c','c','a'], ['a','c','d']))

# exit()

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set_ON, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
