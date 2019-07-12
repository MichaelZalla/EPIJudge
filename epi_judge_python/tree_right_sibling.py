import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def print_levels(root: BinaryTreeNode):

    node, level = root, 0

    while node:

        level_node = node

        print('Level', level, end=': ')

        while level_node:
            print(level_node.data, end=' => ')
            level_node = level_node.next

        print('None')

        node = node.left
        level += 1

def construct_right_sibling_queues(root: BinaryTreeNode) -> None:

    if not root:
        return

    level, next_level = [root], []

    while level:

        for i in range(len(level)):

            node = level[i]

            node.next = level[i+1] if i < len(level) - 1 else None

            if node.left:
                next_level += [node.left, node.right]

        level, next_level = next_level, []

def construct_right_sibling_recursive(root: BinaryTreeNode) -> None:

    if root and root.left:
        root.left.next = root.right

    current_level = 0

    level_start_nodes = {}

    level_start_nodes[current_level] = root

    cursor = level_start_nodes[current_level]

    # While we still have an unprocessed level in the tree...

    while cursor:

        # While we have yet to hit the right-most end at this level...

        while cursor:

            if cursor.left:

                # Populates the next level's starting node, if needed

                if not (current_level + 1) in level_start_nodes:
                    level_start_nodes[current_level + 1] = cursor.left

                # Sets left and right node's 'next' pointers as needed

                cursor.left.next = cursor.right \
                    if cursor.right else None

                if cursor.right:
                    cursor.right.next = cursor.next.left \
                        if cursor.next else None

            # Traverse along this level, moving to the right

            cursor = cursor.next

        # We're done at this level

        current_level += 1

        cursor = level_start_nodes[current_level] \
            if current_level in level_start_nodes else None




# root = BinaryTreeNode(1)
# node2 = BinaryTreeNode(2)
# node3 = BinaryTreeNode(3)
# node4 = BinaryTreeNode(4)
# node5 = BinaryTreeNode(5)
# node6 = BinaryTreeNode(6)
# node7 = BinaryTreeNode(7)

# node3.left = node6
# node3.right = node7

# node2.left = node4
# node2.right = node5

# root.left = node2
# root.right = node3

# construct_right_sibling_recursive(root)

# print_levels(root)

# exit()


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling_recursive, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
