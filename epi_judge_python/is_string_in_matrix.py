from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(A: List[List[int]], S: List[int]) -> bool:

    n, m = len(A), len(A[0])

    # Initialize a subsequence (suffix) table T mirroring the input matrix; if
    # T[i][j] holds an index i in S, this will indicate that, starting at the
    # corresponding cell in A, we can traverse the subsequence (suffix) S[i:]

    contains_subsequence = [[-1] * m for _ in range(n)]

    # Mark those cells that trivially contain the last 1-element subsubsequence
    # (suffix) in S; any cells in A that contain the full sequence S must
    # terminate at one of these cells;

    for j in range(m):
        for i in range(n):
            if A[i][j] == S[-1]:
                contains_subsequence[i][j] = len(S) - 1

    # Locate viable starting points for each subsequently larger suffix

    for suffix_index in reversed(range(len(S) - 1)):

        # Maintain a list of (i,j) coordinates that can begin this suffix

        coordinates = []

        for j in range(m):

            for i in range(n):

                if A[i][j] == S[suffix_index]:

                    # If we use this cell to begin the suffix, can the remainder
                    # of the suffix be visited via neighboring cells?

                    from_left = (j > 0 and \
                        contains_subsequence[i][j-1] == suffix_index + 1)

                    from_right = (j < m-1 and \
                        contains_subsequence[i][j+1] == suffix_index + 1)

                    from_up = (i > 0 and \
                        contains_subsequence[i-1][j] == suffix_index + 1)

                    from_down = (i < n-1 and \
                        contains_subsequence[i+1][j] == suffix_index + 1)

                    if from_up or from_down or from_left or from_right:
                        coordinates.append([i, j])

        # Promote all eligible cells to the next-highest suffix index

        for coordinate in coordinates:
            i, j = coordinate[0], coordinate[1]
            contains_subsequence[i][j] = suffix_index

    # If any cell's suffix index is zero, this indicates that the full sequence
    # can be visited beginning at that cell;

    return any([0 in contains_subsequence[i] for i in range(n)])


# A1 = [[1,2,3],[3,4,5],[5,6,7]]
# S1 = [1,3,4,6]

# print(is_pattern_contained_in_grid(A1, S1))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
