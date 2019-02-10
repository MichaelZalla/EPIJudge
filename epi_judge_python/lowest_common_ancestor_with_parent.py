import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from binary_tree_with_parent_prototype import BinaryTreeNode

def get_lca(n1: BinaryTreeNode,
            n2: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def get_depth(node):

        depth = 0

        while node.parent:
            depth += 1
            node = node.parent

        return depth

    n1_depth, n2_depth = get_depth(n1), get_depth(n2)

    if n1_depth > n2_depth:
        n1, n2 = n2, n1
        n1_depth, n2_depth = n2_depth, n1_depth

    for _ in range(n2_depth - n1_depth):
        n2 = n2.parent

    while n1.parent:

        if n1 is n2:
            return n1

        n1, n2 = n1.parent, n2.parent

    return n1


# F = BinaryTreeNode('F', None, None)
# E = BinaryTreeNode('E', None, None)
# D = BinaryTreeNode('D', F, None)
# C = BinaryTreeNode('C', None, E)
# B = BinaryTreeNode('B', C, D)
# A = BinaryTreeNode('A', None)

# F.parent = D
# E.parent = C
# D.parent = B
# C.parent = B
# B.parent = A

# print(get_lca(E, F))

# exit()


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(get_lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
