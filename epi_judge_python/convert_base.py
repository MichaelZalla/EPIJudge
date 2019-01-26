from test_framework import generic_test

import math, string, functools

HEX_DIGITS = string.hexdigits[:16].upper()

def convert_base_iterative(S: str, b1: int, b2: int) -> str:

    if b1 == b2:
        return S[:]

    base_ten_sum, place, is_negative = 0, 0, (S[0] == '-')

    # Calculate the value of S in decimal

    for i in reversed(range(is_negative, len(S))):

        base_ten_sum += HEX_DIGITS.index(S[i]) * pow(b1, place)

        place += 1

    # Resets place counter

    place = 0

    # Allocates a new digit list of the appropriate length for base b2

    base_b2_digit_count = 1 if base_ten_sum < b2 else math.floor(math.log(base_ten_sum, b2)) + 1

    base_b2_digits = [None] * base_b2_digit_count

    base_ten_remainder = base_ten_sum

    # Iterate backwards through the digits of base_ten_remainder

    for i in reversed(range(base_b2_digit_count)):

        quantity = pow(b2, i)

        digit = base_ten_remainder // quantity

        base_b2_digits[~i] = HEX_DIGITS[digit]

        base_ten_remainder -= (digit * quantity)

    # Sets sign char if needed

    base_b2_string = ('-' if is_negative else '') + ''.join(base_b2_digits)

    return base_b2_string


def convert_base_recursive(S, b1, b2):

    def construct_from_base(n, base):

        if n == 0:
            return ''

        return construct_from_base(n // base, base) + string.hexdigits[n % base].upper()

    is_negative = S[0] == '-'

    n = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        S[is_negative:],
        0)

    return ('-' if is_negative else '') + ('0' if n == 0 else construct_from_base(n, b2))


# print(convert_base_iterative('615', 7, 13))
# print(convert_base_iterative('123', 10, 2))
# print(convert_base_iterative('-1196028', 10, 12))
# print(convert_base_iterative('4', 16, 2))
# print(convert_base_iterative('64', 10, 2))
# print(convert_base_iterative('100000', 3, 3))

# print(convert_base_recursive('615', 7, 13))
# print(convert_base_recursive('123', 10, 2))
# print(convert_base_recursive('-1196028', 10, 12))
# print(convert_base_recursive('4', 16, 2))
# print(convert_base_recursive('64', 10, 2))
# print(convert_base_recursive('100000', 3, 3))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base_iterative))
