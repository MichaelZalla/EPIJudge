from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

from binary_tree_with_parent_prototype import BinaryTreeNode

def inorder_traversal(root: BinaryTreeNode) -> List[int]:

    if not root:
        return []

    if not root.left and not root.right:
        return [root.data]

    result = []

    if root.left:
        curr = root.left
    else:
        curr = root.right
        result = [root.data]

    prev_curr = None

    while True:

        while curr.left:
            curr = curr.left

        result.append(curr.data)

        while not curr.right or curr.right is prev_curr:

            if curr is root:
                return result

            curr, prev_curr = curr.parent, curr

            if curr.right is not prev_curr:
                result.append(curr.data)

            if curr is root and curr.right is prev_curr:
                return result

        curr = curr.right

# H = BinaryTreeNode('H', None, None)
# G = BinaryTreeNode('G', H, None)

# F = BinaryTreeNode('F', None, None)
# E = BinaryTreeNode('E', F, None)
# D = BinaryTreeNode('D', E, G)

# C = BinaryTreeNode('C', None, D)
# B = BinaryTreeNode('B', C, None)
# A = BinaryTreeNode('A', B, None)

# H.parent = G
# G.parent = D
# F.parent = E
# E.parent = D
# D.parent = C
# C.parent = B
# B.parent = A

# print(inorder_traversal(A))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
