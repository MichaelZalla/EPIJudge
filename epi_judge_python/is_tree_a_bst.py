from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def is_binary_tree_bst_minmax(root: BinaryTreeNode,
                                low_range: float=float('-inf'),
                                high_range:float=float('inf')) -> bool:

    # Totally, totally wrong

    if not root:
        return True

    if not root.left and not root.right:
        root.min = root.max = root.data
        return True

    root.min = min(root.data, root.left.min if root.left else high_range, \
        root.right.min if root.right else high_range)

    root.max = max(root.data, root.left.max if root.left else low_range, \
        root.right.max if root.right else low_range)

    return is_binary_tree_bst_minmax(root.left) and is_binary_tree_bst_minmax(root.right) \
        and (root.left.max <= root.data if root.left else True) \
        and (root.right.min >= root.data if root.right else True)

def get_minmax_constraints(root: BinaryTreeNode,
                                low_range: float=float('-inf'),
                                high_range:float=float('inf')) -> bool:

    # Also wrong

    if not root:
        return True

    if not root.left and not root.right:
        return True

    left_constraints = get_minmax_constraints(root.left)
    right_constraints = get_minmax_constraints(root.right)

    if left_constraints[1] <= root.data and right_constraints[0] >= root.data:
        return False

    return [ \
        min(root.data, left_constraints[0], right_constraints[0]), \
        max(root.data, left_constraints[1], right_constraints[1]) \
    ]

def is_binary_tree_bst_recursive(root: BinaryTreeNode,
                                low_range: float=float('-inf'),
                                high_range:float=float('inf')) -> bool:

    if not root:
        return True

    if not (low_range <= root.data and high_range >= root.data):
        return False

    return (is_binary_tree_bst_recursive(root.left, low_range, root.data) \
        and is_binary_tree_bst_recursive(root.right, root.data, high_range))

def is_binary_tree_bst_queue(root: BinaryTreeNode,
                                low_range: float=float('-inf'),
                                high_range:float=float('inf')) -> bool:

    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    queue = collections.deque([
        QueueEntry(root, float('-inf'), float('inf'))
    ])

    while queue:

        front = queue.popleft()

        if front.node:

            if not front.lower <= front.node.data <= front.upper:
                return False

            queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_queue))
