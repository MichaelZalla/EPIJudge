import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


SUDOKU_BOARD_SIZE = 9
SUDOKU_EMPTY_CELL = 0

def get_next_empty_cell(board: List[List[int]]) -> (int, int):

    # O(n) scan through the board, looking for an undecided (0) cell

    for i in range(0, len(board)):
        for j in range(0, SUDOKU_BOARD_SIZE):
            if board[i][j] == SUDOKU_EMPTY_CELL:
                return (i, j)

    return (-1, -1)

def is_valid_choice(board: List[List[int]], i: int, j: int) -> bool:

    def get_region_by_position(board: List[List[int]], i: int, j: int):

        region_digits = []
        region_i_index = (i // 3) * 3
        region_j_index = (j // 3) * 3

        # Uses offsets to collect all cell values in the specified region;

        for i_index in range(region_i_index, region_i_index + 3):
            for j_index in range(region_j_index, region_j_index + 3):
                region_digits.append(board[i_index][j_index])

        return region_digits

    def is_valid_column() -> bool:

        # Checks j-th column for conflicting values

        for j_index in range(0, SUDOKU_BOARD_SIZE):
            if j_index is not j and board[i][j_index] == board[i][j]:
                return False

        return True

    def is_valid_row() -> bool:

        # Checks i-th row for conflicting values

        for i_index in range(0, SUDOKU_BOARD_SIZE):
            if i_index is not i and board[i_index][j] == board[i][j]:
                return False

        return True

    def is_valid_region() -> bool:

        # Checks board[i][j] against all other digits in the board region
        # corresponding to cell (i,j);

        region_i, region_j = i % 3, j % 3

        i_j_region_index = region_i * 3 + region_j

        region_digits = get_region_by_position(board, i, j)

        for index, digit in enumerate(region_digits):
            if not index == i_j_region_index and digit == board[i][j]:
                return False

        return True

    return is_valid_column() and is_valid_row() and is_valid_region()

def solve_sudoku(board: List[List[int]]) -> bool:

    # Check whether there are still undecided cells on our board

    (i, j) = get_next_empty_cell(board)

    if i == -1 and j == -1:

        # If no cells are left undecided, we've arrived at a valid solution

        return True

    # For each digit we might choose for this cell, try it and validate; if
    # the digit is valid choice (assuming no more than one cell in our board
    # may cause conflicts), then we recurse;

    for digit_choice in range(1, 10):

        board[i][j] = digit_choice

        if is_valid_choice(board, i, j):

            #  Recurse to the next undecided cell, if one still exists; the
            #  recursion(s) might return no valid solution, so we check the
            #  final return value;

            result = solve_sudoku(board)

            if result:
                return result

        # Remember to undo our modification to the board before choosing our
        # next digit, or before backtracking to a previous cell;

        board[i][j] = SUDOKU_EMPTY_CELL

    return False


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
