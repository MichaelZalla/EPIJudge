from typing import List

from test_framework import generic_test

import math
import bintrees


def generate_first_k_a_b_sqrt2_naive(k):

    tree = bintrees.AVLTree()

    for a in range(0, k + 1):
        tree.insert(a, (a, 0))

    for b in range(1, k + 1):

        a = 0

        while a < k + 1 and a + b * math.sqrt(2) < tree.max_key():

            tree.pop_max()

            tree.insert(a + b * math.sqrt(2), (a, b))

            a += 1

    return [product for product, a_b_pair in tree.nsmallest(k)]


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:

    result, tree = [], bintrees.AVLTree()

    tree.insert(0, (0, 0))

    while len(result) < k:

        min_node = tree.pop_min()

        min_product, min_a_b = min_node[0], min_node[1]

        result.append(min_product)

        a, b = min_a_b[0], min_a_b[1]

        tree.insert((a + 1) + b * math.sqrt(2), (a + 1, b))
        tree.insert(a + (b + 1) * math.sqrt(2), (a, b + 1))

    return result

# print(generate_first_k_a_b_sqrt2_naive(5))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
