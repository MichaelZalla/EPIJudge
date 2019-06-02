from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:

    results = []

    def permutations_recursive(unchosen, chosen=[]):

        if not unchosen:

            results.append(list(chosen))

            return True

        for index in range(len(unchosen)):

            # At this step, choose the n-th element from the set of unchosen
            # elements

            chosen.append(unchosen.pop(index))

            # Continue choosing until we've generated a complete permutation

            permutations_recursive(unchosen, chosen)

            # Un-choose the last chosen element so we can continue our iteration

            unchosen.insert(index, chosen.pop())

    permutations_recursive(A)

    return results


# print(permutations([]))
# print(permutations([1]))
# print(permutations([1,2]))
# print(permutations([1,2,3]))
# print(permutations([1,2,3,4]))
# print(permutations([1,2,3,4,5]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
