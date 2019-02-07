from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque

def binary_tree_depth_order_twoqueus(root: BinaryTreeNode) -> List[List[int]]:

    result, current_depth = [], deque([root])

    while current_depth:

        next_depth, group_nodes = deque([]), []

        while current_depth:

            current_node = current_depth.popleft()

            if current_node:

                group_nodes.append(current_node.data)

                next_depth += [current_node.left, current_node.right]

        if group_nodes:
            result.append(group_nodes)

        current_depth = next_depth

    return result

def binary_tree_depth_order_onequeue(root: BinaryTreeNode) -> List[List[int]]:

    print(binary_tree_depth_order_averages(root))

    if not root:
        return []

    queue, result = deque([root]), []

    while queue:

        len_queue, group_nodes = len(queue), []

        for _ in range(len_queue):

            if queue[0].left:
                queue.append(queue[0].left)

            if queue[0].right:
                queue.append(queue[0].right)

            group_nodes.append(queue.popleft().data)

        result.append(group_nodes)

    return result

def binary_tree_depth_order_snake(root: BinaryTreeNode) -> List[List[int]]:

    if not root:
        return []

    queue, result, left_to_right = [root], [], False

    while queue:

        left_to_right = not left_to_right

        current_len_queue = len(queue)

        for node in queue[0:current_len_queue]:

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if left_to_right:
            slice = queue[0:current_len_queue]
        else:
            slice = queue[current_len_queue-1::-1]

        result.append(list(
            map(lambda node: node.data, slice)
        ))

        queue = queue[current_len_queue:]

    return result

def binary_tree_depth_order_bottom_up(root: BinaryTreeNode) -> List[List[int]]:

    if not root:
        return []

    queue, result, start_indices, last_end = [root], [], [0], 0

    # Until we run out of nodes to process

    while last_end < len(queue):

        start = last_end

        # last_end is really just beyond the current depth's node group

        last_end = len(queue)

        # Root node will have start=0, last_end=1

        for i in range(start, last_end):

            node = queue[i]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Cache our last_end position for this tree depth (iteration)

        start_indices.append(last_end)

    # Extract sublists of nodes that share the same depth in our queue,
    # advancing backwards (from greater depths to lesser depths)

    # start_indices.append(-1)

    for i in reversed(range(len(start_indices) - 1)):

        # start and end are boundaries of the current depth's node group

        start = start_indices[i]
        end = start_indices[i+1]

        result.append(list(
            map(lambda node: node.data, queue[start:end])
        ))

    return result

def binary_tree_depth_order_averages(root: BinaryTreeNode) -> List[List[int]]:

    if not root:
        return []

    queue, averages = [root], []

    while queue:

        next = []

        depth_data = list(map(lambda node: node.data, queue))

        depth_average = sum(depth_data) / len(depth_data)

        averages.append(depth_average)

        for node in queue:

            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)

        queue = next

    return averages



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order_onequeue))
