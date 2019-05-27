from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:

    i, j, intersection = 0, 0, []

    while i < len(A) and j < len(B):

        if A[i] == B[j]:

            # If this is the first instance of A[i] we've seen, or if we are
            # certain it is not a dupe

            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])

            # Continue scan

            i, j = i + 1, j + 1

        elif A[i] < B[j]:

            # We've encountered the next minimum element in A, or a dupe of
            # A[i-1], but it is not in B

            i += 1

        elif A[i] > B[j]:

            # If the next minimum element in B is not in A, skip over it

            j += 1

    return intersection

def intersect_two_sorted_arrays_fast(A, B):

    result, j = [], 0

    # It's only necessary to scan min(len(A), len(B)) items for intersection

    shorter = A if len(A) <= len(B) else B
    longer = A if B is shorter else B

    for i in range(len(shorter)):

        # Skips duplicates

        if result and result[-1] == shorter[i]:
            continue

        # Advance j until longer[j] >= shorter[i]

        while longer[j] < shorter[i]:

            j += 1

            if j == len(longer):
                return result

        if shorter[i] == longer[j]:

            # We've found a member of the intersection

            result.append(shorter[i])

            j += 1

            if j == len(longer):
                return result

    return result


# A1 = []
# B1 = []

# A2 = []
# B2 = [1,2,3]

# A3 = [1]
# B3 = [1]

# A4 = [1,2,3]
# B4 = [1,2,3]

# A5 = [1,3,5]
# B5 = [2,4,6]

# print(intersect_two_sorted_arrays(A1, B1))
# print(intersect_two_sorted_arrays(A2, B2))
# print(intersect_two_sorted_arrays(A3, B3))
# print(intersect_two_sorted_arrays(A4, B4))
# print(intersect_two_sorted_arrays(A5, B5))

# A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
# B = [5, 5, 6, 8, 8, 9, 10, 10]

# print(intersect_two_sorted_arrays(A, B))

# A = [1, 2, 3, 4]
# B = [1, 4, 5]

# print(intersect_two_sorted_arrays(A, B))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays_fast))
