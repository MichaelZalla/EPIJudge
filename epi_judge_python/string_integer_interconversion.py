from test_framework import generic_test
from test_framework.test_failure import TestFailure

import math, functools, string

# Precomputed int and string lookup structures

# Note that INT_TO_STRING_DIGITS is equal to the built-in constant string.digits

INT_TO_STRING_DIGITS = [ str(digit) for digit in range(0,10) ]

STRING_TO_INT_DIGITS = { key:value for key, value in [(str(digit), digit) for digit in range(0,10)] }

# 1. Converting integer to string

def int_to_string_backfill(n: int) -> str:

    # Zero edge case (cannot take log10 of zero)

    if n == 0:
        return INT_TO_STRING_DIGITS[0]

    # Use log10 to determine number of digits in n (edge case: n < 10)

    digit_count = 1 if abs(n) < 10 else math.floor(math.log10(abs(n)) + 1)

    # Pre-allocates memory for list of length ~digit_count

    chars = [None] * (digit_count if n >= 0 else digit_count + 1)

    # Remainder begins at abs(n) and approaches zero through repeat division

    n_remainder = abs(n)

    # Pull off one decimal digit at a time, adding it to chars

    for i in range(digit_count):

        # Extracts least significant digit from n_remainder

        chars[~i] = INT_TO_STRING_DIGITS[n_remainder % 10]

        # Right-shifts least significant digit out of n_remainder

        n_remainder //= 10

    # Fill the first char with the sign character if necessary

    if chars[0] == None:
        chars[0] = '-'

    # Concatenate chars list into one immutable string

    return ''.join(chars)

def int_to_string_using_code_point(n: int) -> str:

    is_negative = False

    if n < 0:
        n, is_negative = -n, True

    digits = []

    while True:

        # Retrieve the string character corresponding to this decimal digit

        # Note that the Unicode code point (integer) for the digit k is equal to
        # the code point for the digit zero, plus k

        digit = chr(ord('0') + n % 10)

        digits.append(digit)

        # Right-shifts the least significant digit in n

        n //= 10

        # If n == 0, then we've consumed the last available digit

        if n == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(digits))

# 2. Converting string to integer

def string_to_int_add(s: str) -> int:

    result, shift = 0, 0

    # For each char position in s, beginning at the last position

    for i in reversed(range(len(s))):

        # Edge case where we reach the sign char

        if s[i] == '-':

            result *= -1

        else:

            # Map the digit character to an integer value

            digit = STRING_TO_INT_DIGITS[s[i]]

            # Add to result

            result += digit*pow(10, shift)

        # We increase place as we move from right to left

        shift += 1

    return result

def string_to_int_multiply(s: str) -> int:

    is_negative = s[0] == '-'

    # Uses functools.reduce with lambda, iterable, and initial value

    digits = s[1 if is_negative else 0:]

    absolute_value = functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        digits,
        0
    )

    # Flips sign if needed

    return absolute_value * (-1 if is_negative else 1)


# print(int_to_string_backfill(0))
# print(int_to_string_backfill(0))

# print(int_to_string_backfill(1))
# print(int_to_string_backfill(-1))

# print(int_to_string_backfill(10))
# print(int_to_string_backfill(-10))

# print(int_to_string_backfill(99))
# print(int_to_string_backfill(-99))

# print(int_to_string_backfill(100))
# print(int_to_string_backfill(-100))

# print(int_to_string_backfill(1234567890))
# print(int_to_string_backfill(-1234567890))

# exit()

def wrapper(x, s):
    if int(int_to_string_backfill(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int_add(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
