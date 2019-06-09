from test_framework import generic_test


def count_traversals(n: int, m: int) -> int:

    # In a single dimension, there is exactly 1 way to reach the endpoint

    traversal_counts = [[1] * m if i == 0 else [1] + [0] * (m-1) for i in range(n)]

    # If this isn't actually a 2-dimensional matrix, we already have our answer

    if n > 1 or m > 1:

        # We can compute our subtraversal table in either row-first or
        # column-first priority; the order here doesn't matter;

        for j in range(1, m):

            for i in range(1, n):

                # There are two possible ways to complete a given traversal: our
                # last move could either have been a right-move or a down-move;

                # Either move would have us starting from some original position
                # that corresponds to a u-by-v submatrix for which we have
                # already calculated the number of possible traversals that can
                # reach that position;

                traversal_counts[i][j] = \
                    traversal_counts[i-1][j] + traversal_counts[i][j-1]

    # The bottom-right cell in our subtraversal table holds the number of
    # possible traversals that reach the endpoint in an n-by-m matrix;

    return traversal_counts[-1][-1]


# n, m = 1, 1
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 1, 2
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 2, 1
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 2, 2
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 1, 7
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 6, 1
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 6, 4
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 4, 5
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 5, 7
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# n, m = 6, 7
# print('Number of traversals for an {}-by-{} matrix: {}'.format(n, m, count_traversals(n,m)))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       count_traversals))
