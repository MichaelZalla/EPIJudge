from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(root: BinaryTreeNode, partial_path_sum:int=0) -> int:

    if not root:
        return 0

    partial_path_sum = 2 * partial_path_sum + root.data

    if not root.left and not root.right:
        return partial_path_sum

    return sum_root_to_leaf(root.left, partial_path_sum) + \
        sum_root_to_leaf(root.right, partial_path_sum)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
