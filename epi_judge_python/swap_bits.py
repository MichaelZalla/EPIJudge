from test_framework import generic_test

def swap_bits_pow(x, i, j):

	ibit = (x >> i) & 1
	jbit = (x >> j) & 1

	# print('ibit: %d' % ibit)
	# print('jbit: %d' % jbit)

	if ibit is not jbit:

		twoToI = 2**i
		twoToJ = 2**j

		if ibit:

			x = x - twoToI + twoToJ

		else:

			x = x - twoToJ + twoToI

	return x

def swap_bits_xor(x, i, j):

	if (x >> i) & 1 != (x >> j) & 1:

		x ^= (1 << i | 1 << j)

	return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits_xor))
