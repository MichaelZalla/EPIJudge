from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from binary_tree_node import BinaryTreeNode

# from binarytree import build

def is_symmetric(node: BinaryTreeNode) -> bool:

    def is_pair_symmetric(left, right):

        if left or right:

            if bool(left and not right):
                return False

            if bool(right and not left):
                return False

            if left.data != right.data:
                return False

            if bool(left.left or right.right) and not is_pair_symmetric(left.left, right.right):
                return False

            if bool(left.right or right.left) and not is_pair_symmetric(right.left, left.right):
                return False

        return True

    return not node or is_pair_symmetric(node.left, node.right)


def is_symmetric_compact(node: BinaryTreeNode) -> bool:

    def is_pair_symmetric(subtree_0, subtree_1):

        if not subtree_0 and not subtree_1:
            return True

        elif subtree_0 and subtree_1:
            return (\
                subtree_0.data == subtree_1.data and \
                is_pair_symmetric(subtree_0.left, subtree_1.right) and \
                is_pair_symmetric(subtree_0.right, subtree_1.left))

        return False

    return not node or is_pair_symmetric(node.left, node.right)

# left_right = BinaryTreeNode(7)
# right_left = BinaryTreeNode(7)

# left = BinaryTreeNode(5, None, left_right)
# right = BinaryTreeNode(5, right_left, None)

# root = BinaryTreeNode(4, left, right)

# print(is_symmetric(root))

# values = [0,-3,0,-11,-7,2,7,-5,2,0,1,0,1,1,-12,1,-5,-3,-3,12,-2,-10,4,8,7,7,1,-4,-6,-8,-12]

# tree = build(values)

# print(tree)

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
