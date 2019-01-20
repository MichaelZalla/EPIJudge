from test_framework import generic_test

def add(x, y):

	sum = 0
	mask = 1
	carry = 0
	remain = x | y

	while remain or carry:

		# XOR the digits in x and y with the carry bit

		xbit = x & mask
		ybit = y & mask

		new_bit = xbit ^ ybit ^ carry

		# print("{0:b}".format(remain))

		remain &= ~mask

		# OR the new bit into sum

		sum |= new_bit

		# Advance our mask by one place

		mask <<= 1

		# Test whether we should set the carry bit for the next iteration

		if (xbit and ybit) or ((xbit or ybit) and carry):

			# Carry bit is placed in the mask's new place

			carry = mask

		else:

			carry = 0

	return sum

def multiply(x: int, y: int) -> int:

	product = 0

	# Starts at the 0-th bit in y

	mask = 1
	mask_bit_index = 0

	# We will unset the set bits in y until y becomes zero

	while y:

		# Checks whether our y contains the quantity 2**i

		if mask & y:

			# Contributes x*(2**i) to our product

			product = add(product, x << mask_bit_index)

		# Clears the i-th bit in y

		y &= ~mask

		# Updates our mask variables

		mask <<= 1

		mask_bit_index = add(mask_bit_index, 1)

	return product

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
