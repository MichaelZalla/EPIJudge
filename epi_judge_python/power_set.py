from typing import List

from test_framework import generic_test, test_utils

import math

def generate_power_set(S: List[int]) -> List[List[int]]:

    def generate_power_set_incremental(S, last_unvisited):

        # If last_unvisited no longer points to a valid element index in S, then
        # we can assume that all elements are accounted for in the current call
        # stack; we need only to return the empty set;

        if last_unvisited == -1:
            return [[]]

        # To compute the power set P of S, we do the following:
        #
        # We remove the last element e from S and recursively compute the power
        # set P' of the resulting new set S'; we then return the union P' + [p +
        # e for all p in P']; we transform P' into P by additionally
        # representing e in each set contained in P';

        sub_power_set = generate_power_set_incremental(S, last_unvisited - 1)

        sub_power_set_plus_unvisited = [s + [S[last_unvisited]] for s in sub_power_set]

        return sub_power_set + sub_power_set_plus_unvisited

    return generate_power_set_incremental(S, len(S) - 1)

def generate_power_set_bitfield(S):

    power_set = []

    for bit_field in range(1 << len(S)):

        subset = []

        while bit_field:

            # Mask out any lower set bits

            masked_highest_bit = bit_field & ~(bit_field - 1)

            # Calculate the bit index of the bit

            bit_index = int(math.log2(masked_highest_bit))

            # Add the corresponding element in S to the subset we're generating

            subset.append(S[bit_index])

            bit_field &= bit_field - 1

        power_set.append(subset)

    return power_set

# print(generate_power_set([]))
# print(generate_power_set([1]))
# print(generate_power_set([1,2]))
# print(generate_power_set([1,2,3]))
# print(generate_power_set([1,2,3,4]))
# print(generate_power_set([1,2,3,4,5]))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
