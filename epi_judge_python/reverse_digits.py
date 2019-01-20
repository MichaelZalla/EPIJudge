from test_framework import generic_test

def reverse(x: int) -> int:

    result = 0

    x_remaining = abs(x)

    # We'll strip away one digit from x at a time until x is zero

    while x_remaining:

        # Left-shift any existing digits in our result

        result *= 10

        # Adds the least significant digit of x (currently) to our result

        result += x_remaining % 10

        # Right-shifts the remaining (unvisited) digits of x, dropping the last
        # visited digit

        x_remaining //= 10

    return -result if x < 0 else result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
