from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(node: BinaryTreeNode, remaining_weight: int) -> bool:

    if not node:
        return False

    # if node.data > remaining_weight:
    #     return False

    if not node.left and not node.right and node.data == remaining_weight:
        return True

    return has_path_sum(node.left, remaining_weight - node.data) or \
        has_path_sum(node.right, remaining_weight - node.data)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
