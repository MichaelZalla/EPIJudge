from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:

	lower, upper = 0, len(A) - 1

	while lower < upper:

		mid = lower + (upper-lower)//2

		if A[mid] >= k:
			upper = mid
		else:
			lower = mid+1

	if lower < len(A) and A[lower] == k:
		return lower

	return -1


# A = []
# B = [0]
# C = [1]
# D = [1,1,1]
# E = [0,1,2]
# F = [0,0,1,1,1,3,3,7,9]

# k = 1

# print(search_first_of_k(A, k))
# print(search_first_of_k(B, k))
# print(search_first_of_k(C, k))
# print(search_first_of_k(D, k))
# print(search_first_of_k(E, k))
# print(search_first_of_k(F, k))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
