from test_framework import generic_test

def closest_binary_weighted_integer(x: int) -> int:

	NUM_UNSINGED_BITS = 64

	for i in range(0, NUM_UNSINGED_BITS - 1):

		# Isolates bit values for comparison
		if (x >> i) & 1 != (x >> (i + 1)) & 1:

			return x ^ ((1 << i) | (1 << (i + 1)))

	raise ValueError("All bits are zero or one!")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_binary_weighted_integer))
