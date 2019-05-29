from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(root: BstNode,
                                k: int,
                                last_largest_node: BstNode = None) -> Optional[BstNode]:

    if not root:
        return last_largest_node

    if root.data <= k:
        return find_first_greater_than_k(root.right, k, last_largest_node)
    else:
        return find_first_greater_than_k(root.left, k, root)

def find_first_greater_than_k_iterative(root, k):

    subtree, last_largest_node = root, None

    while subtree:

        if subtree.data > k:
            last_largest_node, subtree = subtree, subtree.left
        else:
            subtree = subtree.right

    return last_largest_node


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
