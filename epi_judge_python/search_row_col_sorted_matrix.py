from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:

    row, col = 0, len(A[0]) - 1

    # Row index will increase during search, column index will decrease;

    while row < len(A) and col > -1:

        if A[row][col] < x:

            # We can ignore this entire row

            row += 1

        elif A[row][col] > x:

            # We can ignore this entire column

            col -= 1

        else:

            return True

    # We exhausted all rows and columns without finding x

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
