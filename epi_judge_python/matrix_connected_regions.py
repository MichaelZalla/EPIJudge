from typing import List

from test_framework import generic_test

import collections

def flip_color(x: int, y: int, M: List[List[bool]]) -> None:

    def get_fill_neighbors(x, y):

        color, n = M[x][y], []

        # Checks to the left
        if x > 0 and M[x-1][y] == color:
            n.append([x-1, y])

        # Checks to the right
        if x < len(M) - 1 and M[x+1][y] == color:
            n.append([x+1, y])

        # Checks above
        if y > 0 and M[x][y-1] == color:
            n.append([x, y-1])

        # Checks below
        if y < len(M[0]) - 1 and M[x][y+1] == color:
            n.append([x, y+1])

        return n

    start = [x,y]

    # We'll track all unseen pixels, as well as seen pixels that are either
    # flipped or scheduled to be flipped

    # Graph BFS means that we'll 'visit' pixels in least-recently-seen-first
    # order

    frontier, scheduled = collections.deque([start]), {}

    while frontier:

        x, y = frontier.popleft()

        # Checks for adjacent same-color pixels that have not been scheduled

        neighbors = [n for n in get_fill_neighbors(x, y) if str(n) not in scheduled]

        for neighbor in neighbors:

            # Schedules the pixels to be flipped later

            frontier.append(neighbor)

            # Mark this pixel as 'scheduled'

            scheduled[str(neighbor)] = True

        # Flip this pixel's color

        M[x][y] = (0 if M[x][y] else 1)

    return

# M1 = [
#     [1,1,0,0,1,1],
#     [1,0,1,1,1,1],
#     [0,1,0,0,0,0],
#     [0,1,0,0,1,0],
#     [0,0,0,1,0,1],
#     [0,1,0,1,0,1],
# ]

# flip_color(3,3, M1)

# for row in M1:
#     print(row)

# exit()


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
