from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:

    # Negative integers cannot be palindromes by definition

    if x < 0:
        return False

    if x == 0:
        return True

    # Computes the number of significant digits in x

    num_digits = math.floor(math.log10(x)) + 1

    # Creates a decimal digit mask, isolating the most significant digit in x

    msd_mask = 10 ** (num_digits - 1)

    # Iterates through num_digits // 2

    for i in range(num_digits // 2):

        # Tests whether the MSD matches the LSD

        if x // msd_mask != x % 10:
            return False

        # Drops the MSD and LSD from our value

        x %= msd_mask
        x //= 10

        # Reduces our mask by 10**2

        msd_mask //= 10**2

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
