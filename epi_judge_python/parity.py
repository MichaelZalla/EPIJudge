from test_framework import generic_test

def compute_parity_brute(x: int) -> int:

	result = 0

	while x:

		result ^= x & 1

		x >>= 1

	return result

def compute_parity_lsb(x: int) -> int:

	result = 0

	while x:

		x &= x - 1

		result ^= 1

	return result

def compute_parity_cache(x: int) -> int:

	# @TODO(mzalla) Implementation

    return

def compute_parity_compress(x: int) -> int:

	x ^= x >> 32 # compress to least significant 32 bits
	x ^= x >> 16 # compress to least significant 16 bits
	x ^= x >> 8  # ... 8 bits
	x ^= x >> 4  # ... 4 bits
	x ^= x >> 2  # ... 2 bits
	x ^= x >> 1  # ... bit

	return x & 1

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', compute_parity_compress))
