from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from binary_tree_node import BinaryTreeNode

def inorder_traversal(node: BinaryTreeNode) -> List[int]:

    def get_traversal_record(node):
        return { 'node': node, 'left_visited': False, 'right_visited': False }

    if not node:
        return []

    stack, result = [get_traversal_record(node)], []

    while stack:

        record = stack[-1]

        node = record['node']

        if record['left_visited'] and record['right_visited']:
            stack.pop()
            continue

        if not record['left_visited']:
            if node.left:
                stack.append(get_traversal_record(node.left))
            record['left_visited'] = True
            continue

        result.append(node.data)

        if not record['right_visited']:
            if node.right:
                stack.append(get_traversal_record(node.right))
            record['right_visited'] = True

    return result


# D = BinaryTreeNode('D')
# E = BinaryTreeNode('E', D)
# B = BinaryTreeNode('B', None, E)

# H = BinaryTreeNode('H')
# G = BinaryTreeNode('G', None, H)
# F = BinaryTreeNode('F')
# C = BinaryTreeNode('C', F, G)

# A = BinaryTreeNode('A', B, C)

# print(inorder_traversal(A))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
