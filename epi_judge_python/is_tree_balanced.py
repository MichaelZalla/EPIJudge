from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

import collections

def is_height_balanced(node: BinaryTreeNode) -> bool:

    if not node:
        return True

    def has_left_leg(node):
        return bool(node.left and (not node.right) and \
            (node.left.left or node.left.right))

    def has_right_leg(node):
        return bool(node.right and (not node.left) and \
            (node.right.left or node.right.right))

    return bool(is_height_balanced(node.left) and \
        is_height_balanced(node.right) and \
        not has_left_leg(node) and not has_right_leg(node))

# # 1A

# node1 = BinaryTreeNode(1)
# node2 = BinaryTreeNode(1, node1)
# node3 = BinaryTreeNode(1, node2)

# # 1B

# node4 = BinaryTreeNode(1)
# node5 = BinaryTreeNode(1, None, node4)
# node6 = BinaryTreeNode(1, node5)

# # 2A

# node7 = BinaryTreeNode(1, None)
# node8 = BinaryTreeNode(1, None, node7)
# node9 = BinaryTreeNode(1, None, node8)

# # 2B

# node10 = BinaryTreeNode(1)
# node11 = BinaryTreeNode(1, node10)
# node12 = BinaryTreeNode(1, None, node11)

# # Root

# print(has_left_leg(node3), has_right_leg(node3))
# print(has_left_leg(node6), has_right_leg(node6))
# print(has_left_leg(node9), has_right_leg(node9))
# print(has_left_leg(node12), has_right_leg(node12))

# print(is_height_balanced(node3))
# print(is_height_balanced(node6))
# print(is_height_balanced(node9))
# print(is_height_balanced(node12))

# print(is_height_balanced(root))

# exit()

def is_height_balanced_cache(node: BinaryTreeNode) -> bool:

    BalancedStatusWithHeight = collections.namedtuple( \
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(node: BinaryTreeNode) -> bool:

        if not node:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(node.left)

        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(node.right)

        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1

        height = max(left_result.height, right_result.height) + 1

        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(node).balanced



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_height_balanced))
