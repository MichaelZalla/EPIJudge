from typing import List

from test_framework import generic_test


def apply_permutation(P: List[int], A: List[int]) -> None:

    for i in range(len(A)):

        # Element A[i] will be moving to index P[i]

        next = i

        # While P[next] points to an unvisited element in this cycle...

        while P[next] >= 0:

            # Move A[i] into A[P[next]]; temporarily store whatever value was at
            # A[P[next]] at the 'hole' created at A[i];

            A[i], A[P[next]] = A[P[next]], A[i]

            # Store P[next] (next destination index) temporarily before we
            # overwrite P[next]; we use a constant offset to maintain the
            # original, relative ordering of P-indices while simultaneously
            # marking the P-index as 'completed';

            temp = P[next]

            P[next] -= len(P)

            next = temp

    # Restores the original indices in P by adding back the constant offset;

    P[:] = [i + len(P) for i in P]

    return


# A, P = ['a','b','c','d',], [2,0,1,3]

# apply_permutation(P, A)

# print(A, P)

# exit()


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
