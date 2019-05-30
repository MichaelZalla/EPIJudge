from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst_stack(tree: BstNode, k: int) -> List[int]:

    k_largest = []

    # Iterative reverse-order traversal using a stack

    current, stack, finished_traversal = tree, [], False

    # Can't perform stack empty check here (first iteration, stack is empty)
    # Checking length of k_largest allows us to short-circuit the traversal

    while not finished_traversal and len(k_largest) < k:

        if current:

            # Add current node to the stack, and (naively) move to the right

            stack.append(current)

            current = current.right

        elif stack:

            # Current does not point to any node; we may have traversed past a
            # leaf node towards the right or towards the left (into None-land);

            # Backtrack our 'current' reference to the node that was last seen;

            current = stack.pop()

            # Reverse-order traversal means that this node must belong in k_largest;

            k_largest.append(current.data)

            # Naively move to the left

            current = current.left

        else:

            # Nothing left in the stack, so we've visited all nodes in the tree;

            finished_traversal = True

    # Returns largest min(k, n) keys

    return k_largest

def find_k_largest_in_bst_recursive(tree, k):

    def find_k_largest_in_bst_recursive_helper(tree):

        if tree and len(k_largest) < k:

            find_k_largest_in_bst_recursive_helper(tree.right)

            if len(k_largest) < k:

                k_largest.append(tree.data)

                find_k_largest_in_bst_recursive_helper(tree.left)


    k_largest = []

    find_k_largest_in_bst_recursive_helper(tree)

    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst_stack,
                                       test_utils.unordered_compare))
