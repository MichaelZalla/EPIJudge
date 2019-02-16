from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from binary_tree_node import BinaryTreeNode

def get_tree_from_preorder_inorder(preorder: List[int],
                                    inorder: List[int]) -> BinaryTreeNode:

    # We can assume inorder and preorder lists have equal length

    num_elems = len(inorder)

    if not num_elems:
        # Empty subtree
        return None

    if num_elems == 1:
        # Shortcut (skips recursive calls)
        return BinaryTreeNode(inorder[0], None, None)

    # Determine root, left subtree, and right subtree elements

    root = preorder[0]

    root_index = inorder.index(root)

    left_inorder = inorder[0:root_index]

    if root_index == num_elems - 1:
        right_inorder = []
    else:
        right_inorder = inorder[root_index + 1:]

    left_preorder = [key for key in preorder if key in left_inorder]
    right_preorder = [key for key in preorder if key in right_inorder]

    # Left and right recursive calls

    return BinaryTreeNode(root, \
        get_tree_from_preorder_inorder(left_preorder, left_inorder), \
        get_tree_from_preorder_inorder(right_preorder, right_inorder) \
    )


# inorder = ['D','B','G','E','A','C','F']
# preorder = ['A','B','D','E','G','C','F']

# print(get_tree_from_preorder_inorder(preorder, inorder))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       get_tree_from_preorder_inorder))
