import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from binary_tree_node import BinaryTreeNode

def get_lca(root: BinaryTreeNode,
            n1: BinaryTreeNode,
            n2: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def is_descendent(ancestor, node):

        if not ancestor:
            return False

        if node is ancestor:
            return True

        return is_descendent(ancestor.left, node) or \
            is_descendent(ancestor.right, node)

    if n1 is n2:
        return n1

    if root is n1 or root is n2:
        return root

    left_has_n1 = is_descendent(root.left, n1)
    left_has_n2 = is_descendent(root.left, n2)

    # A. n1 and n2 in left subtree

    if left_has_n1 and left_has_n2:
        return get_lca(root.left, n1, n2)

    right_has_n1 = is_descendent(root.right, n1)

    # B. n2 in left subtree and n1 in right subtree (root is LCA)

    if left_has_n2 and right_has_n1:
        return root

    right_has_n2 = is_descendent(root.right, n2)

    # C. n1 in left subtree and n2 in right subtree (root is LCA)

    if left_has_n1 and right_has_n2:
        return root

    # D. n1 and n2 in right subtree

    if right_has_n1 and right_has_n2:
        return get_lca(root.right, n1, n2)

    # E. root does not hold both nodes (no LCA)

    return None

# left_right_left = BinaryTreeNode('Q')
# left_right_right = BinaryTreeNode('Q')

# left_right = BinaryTreeNode('M', left_right_left, left_right_right)

# left = BinaryTreeNode('I', None, left_right)
# right = BinaryTreeNode('N')

# root = BinaryTreeNode('K', left, right)

# print(get_lca(root, left_right_left, left_right_right))

# exit()

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(get_lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
