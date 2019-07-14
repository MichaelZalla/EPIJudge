import functools
from typing import List

import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:

    # Compute (missing ^ duplicate) using the XOR summation of [0, n-1] and A;
    # we compute this sum pair-wise using elements from the sets [0, n-1] and A;

    missing_xor_dup = functools.reduce(
        lambda x, i: x ^ i[0] ^ i[1],
        enumerate(A),
        0)

    # Determine the lowest set bit in missing_xor_dup; this will be a bit that
    # differs between 'missing' and 'duplicate';

    least_significant_bit = missing_xor_dup & (~(missing_xor_dup -1))

    # Extract either the missing or duplicate value by taking the XOR summation
    # of the two sets:
    #
    # S1 = { i | i & lsb, 0 <= i <= (n-1) }
    # S2 = { a | a & lsb, a in A };
    #

    missing_or_dup = 0

    for i, v in enumerate(A):
        if i & least_significant_bit:
            missing_or_dup ^= i
        if v & least_significant_bit:
            missing_or_dup ^= v

    # At this point, we can determine whether we've found the missing element or
    # the duplicate element by comparing the value we extracted above with the
    # values in A;

    if missing_or_dup in A:

        duplicate = missing_or_dup
        missing = missing_xor_dup ^ missing_or_dup

        return DuplicateAndMissing(duplicate, missing)

    else:

        duplicate = missing_xor_dup ^ missing_or_dup
        missing = missing_or_dup

        return DuplicateAndMissing(duplicate, missing)


# print(find_duplicate_missing([1,1]))
# print(find_duplicate_missing([0,1,3,3]))
# print(find_duplicate_missing([0,1,2,4,4,5]))
# print(find_duplicate_missing([1,4,2,5,4,0]))

# exit()

def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
