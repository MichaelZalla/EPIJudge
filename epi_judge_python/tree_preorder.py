from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from binary_tree_node import BinaryTreeNode

def preorder_traversal(root: BinaryTreeNode) -> List[int]:

    if not root:
        return []

    stack, result = [root], []

    while stack:

        node = stack.pop()

        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result

# H = BinaryTreeNode('H')
# F = BinaryTreeNode('F', None, H)
# E = BinaryTreeNode('E')
# C = BinaryTreeNode('C', E, F)


# G = BinaryTreeNode('G')
# D = BinaryTreeNode('D', G)
# B = BinaryTreeNode('B', None, D)
# A = BinaryTreeNode('A', B, C)

# print(preorder_traversal(A))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
