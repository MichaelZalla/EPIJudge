from typing import List

from test_framework import generic_test

import math

def can_reach_end_backtrack(A: List[int]) -> bool:

    if len(A) < 2:
        return True

    debt = 1

    A.pop()

    while A:

        budget = A.pop()

        if budget >= debt:
            debt = max(0, debt - budget)

        debt += 1

    if debt > budget or budget == 0:
        return False

    else:
        return True

def can_reach_end_frontier(A):

    furthest_reachable, finish_line = 0, len(A) - 1

    index = 0

    while index <= furthest_reachable and furthest_reachable < finish_line:

        furthest_reachable = max(furthest_reachable, index + A[index])

        index += 1

    return furthest_reachable >= finish_line

def shortest_num_moves(A):

    start_index, finish_index, node_count = 0, len(A) - 1, len(A)

    visited, frontier = [], [start_index]

    cache = [[0 if x == y else math.inf for x in range(node_count)] for y in range(node_count)]

    while frontier:

        src_index = frontier.pop()

        # If we haven't visited this node before

        if src_index in visited:
            continue

        moves = A[src_index]

        for i in range(1, moves + 1):

            # Each potential 'move' constitutes a directed edge from node
            # src_index to node (src_index+i)
            # Ignore moves that are out-of-bounds

            dest_index = src_index + i

            if dest_index > finish_index:
                continue

            # Update cache if we can get to dest_index faster (cache[src_index] + i)

            existing_cost = cache[start_index][dest_index]

            potential_cost = cache[start_index][src_index] + 1

            if potential_cost < existing_cost:

                cache[start_index][dest_index] = potential_cost

            # Add node dest_index to the frontier if we have yet to visit it

            if dest_index not in frontier:

                frontier.append(dest_index)

        # Add the current node to our list of 'visited' nodes

        visited.append(src_index)

    shortest_path = cache[start_index][finish_index]

    return shortest_path

# print(shortest_num_moves([1,2,0,3,1,0,4]))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end_backtrack))
