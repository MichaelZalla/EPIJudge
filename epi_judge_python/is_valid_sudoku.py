from typing import List

from test_framework import generic_test

import math

SUDOKU_BOARD_SIZE = 9

SUDOKU_SUBGRID_SIZE = int(math.sqrt(SUDOKU_BOARD_SIZE))

def is_valid_sudoku(board: List[List[int]]) -> bool:

    # Asserts that all non-zero cell values in the list input are unique

    def unique(cells):

        cells = list(filter(lambda digit: digit != 0, cells))

        return len(cells) == len(set(cells))

    # Checks unique row-wise and column-wise lists of (non-empty) cells

    if not all([
        unique([ board[i][j] for j in range(SUDOKU_BOARD_SIZE) ]) and
        unique([ board[j][i] for j in range(SUDOKU_BOARD_SIZE) ])
        for i in range(SUDOKU_BOARD_SIZE)]):

        return False

    # Checks unique subgrid-wise lists of (non-empty) cells

    # I => [0..3]
    # J => [0..3]

    # i => [0..3], [3..6], [6..9]
    # j => [0..3], [3..6], [6..9]

    return all([
        unique([
            board[i][j]
            for i in range(SUDOKU_SUBGRID_SIZE * I, SUDOKU_SUBGRID_SIZE * (I + 1))
            for j in range(SUDOKU_SUBGRID_SIZE * J, SUDOKU_SUBGRID_SIZE * (J + 1))
        ])
        for I in range(SUDOKU_SUBGRID_SIZE)
        for J in range(SUDOKU_SUBGRID_SIZE)
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
