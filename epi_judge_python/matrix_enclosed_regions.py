import collections
from typing import List

from test_framework import generic_test

def print_matrix(M):

    for row in range(len(M)):
        print(row)

    return

W, B = 'W', 'B'

def fill_surrounded_regions(M: List[List[str]]) -> None:

    def get_matching_neighbors(row, col):

        color, neighbors = M[row][col], []

        # Check to the left
        if col > 0 and M[row][col-1] == color:
            neighbors.append([row, col-1])

        # Check to the right
        if col < len(M[0]) - 1 and M[row][col+1] == color:
            neighbors.append([row, col+1])

        # Check above
        if row > 0 and M[row-1][col] == color:
            neighbors.append([row-1, col])

        # Check below
        if row < len(M) - 1 and M[row+1][col] == color:
            neighbors.append([row+1, col])

        return neighbors

    def get_fill_region(row, col):

        start = [row, col]

        region, frontier, visited = [], collections.deque([start]), {}

        while frontier:

            row, col = frontier.popleft()

            # Visit this coordinate

            region.append([row, col])

            visited[str([row, col])] = True

            # Add any same-color adjacent coordinates that have not been seen

            for neighbor in [n for n in get_matching_neighbors(row, col) if str(n) not in visited]:
                frontier.append(neighbor)

        return region

    def add_fill_region(row, col):

        fill_region = get_fill_region(row, col)

        for row, col in fill_region:
            B[row][col] = True

        return

    m, n = len(M), len(M[0])

    # Build a bitmap encoding all edge regions in our board

    B = [[False] * n for _ in range(m)]

    for col in range(0, n):

        if M[0][col] == 'W' and not B[0][col]:
            add_fill_region(0, col)

        if M[m-1][col] == 'W' and not B[m-1][col]:
            add_fill_region(m-1, col)

    for row in range(1, m-1):

        if M[row][0] == 'W' and not B[row][0]:
            add_fill_region(row, 0)

        if M[row][n-1] == 'W' and not B[row][n-1]:
            add_fill_region(row, n-1)

    # Iterate through the board, flipping any W entries that are not marked in B

    for row in range(m):
        for col in range(n):
            if M[row][col] == 'W' and not B[row][col]:
                M[row][col] = 'B'

    # Finished

    return


# # Test for 4x4 board

# M1 = [
#     [B,B,B,B],
#     [W,B,W,B],
#     [B,W,W,B],
#     [B,B,B,B],
# ]

# fill_surrounded_regions(M1)

# print_matrix(M1)

# # Test for 6x6 board

# M2 = [
#     [W,B,B,B,B,B],
#     [W,B,W,W,W,B],
#     [B,B,B,B,W,B],
#     [B,W,W,B,B,W],
#     [B,W,B,W,W,B],
#     [B,B,B,W,B,B],
# ]

# fill_surrounded_regions(M2)

# print_matrix(M2)

# exit()


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
