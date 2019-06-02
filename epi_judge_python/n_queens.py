from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:

    # Constructs an n x n 'board' on which to place our queens

    B, solutions = [-1] * n, []

    n_queens_backtrack(B, n, solutions, 0)

    return solutions

def reject(B, col_index):

    # For all preceeding columns in our board

    for i in range(col_index):

        # Assert that no two queens are placed in the same row, and that no
        # placed queens are diagonal to the potential queen;

        # print('Testing potential queen at column {}...'.format(col_index))

        if B[i] == B[col_index] or col_index - i == abs(B[col_index] - B[i]):
            return True

    # All clear
    return False

def n_queens_backtrack(B, n, solutions, column_index):

    if column_index == n:

        # We've found a complete solution! (n == last column index + 1)

        solutions.append(B.copy())

        return True

    for row_index in range(n):

        B[column_index] = row_index

        if not reject(B, column_index):

            # has_solution =
            n_queens_backtrack(B, n, solutions, column_index + 1)

            # if has_solution:
            #     return True

    # return False

# print('For n=0:')
# print(n_queens(0), end='\n\n')

# print('For n=1:')
# print(n_queens(1), end='\n\n')

# print('For n=2:')
# print(n_queens(2), end='\n\n')

# print('For n=3:')
# print(n_queens(3), end='\n\n')

# print('For n=4:')
# print(n_queens(4))
# print()

# print('For n=5:')
# print(n_queens(5))
# print()

# print('For n=6:')
# print(n_queens(6))
# print()

# print('For n=7:')
# print(n_queens(7))
# print()

# print('For n=8:')
# print(n_queens(8))
# print()

# exit()


def comp(a, b):
    return sorted(a) == sorted(b)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
