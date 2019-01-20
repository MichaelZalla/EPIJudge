from test_framework import generic_test

def power(x: float, y: int) -> float:

    result = 1.0

    # Adjusts our starting values if y is negative

    if y < 0:
        y = -y
        x = 1.0 / x

    # We'll "reduce" our y by powers-of-two, and double 'product' as we visit
    # each digit position in y

    product = x

    # Our y will eventually be right-shifted to zero

    while y:

        # If the current bit in y is set, multiply by our running product

        if y & 1:
            result *= product

        # Doubles our running multiple of x for the current digit postion

        product = product*product

        # Right-shifts our y

        y >>= 1

    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
