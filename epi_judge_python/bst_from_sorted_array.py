import functools
from typing import List, Optional

from bst_node import BstNode
from binary_tree_node import BinaryTreeNode

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:

    def build_min_height_bst_from_sorted_array_range(A, start, end):

        if start > end:
            return None

        mid_index = (start + end) // 2

        node = BinaryTreeNode(A[mid_index])

        node.left = build_min_height_bst_from_sorted_array_range(A, start, mid_index - 1)
        node.right = build_min_height_bst_from_sorted_array_range(A, mid_index + 1, end)

        return node

    return build_min_height_bst_from_sorted_array_range(A, 0, len(A) - 1)


# print(build_min_height_bst_from_sorted_array([]))
# print(build_min_height_bst_from_sorted_array([2]))
# print(build_min_height_bst_from_sorted_array([1,1,1,1,1,1,1]))
# print(build_min_height_bst_from_sorted_array([2,3,4,6,8,9,11]))

# exit()

@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
