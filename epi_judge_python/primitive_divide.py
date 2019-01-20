from test_framework import generic_test

def divide(x: int, y: int) -> int:

    quotient = 0

    power_of_two = 32

    y_to_power = y << power_of_two

    while x >= y:

        # Finds the largest integer of the form y*(2**power_of_two) | integer < x

        while y_to_power > x:

            power_of_two -= 1

            y_to_power >>= 1

        # Removes y_to_power from x, adding (2**power_of_two) to our quotient;

        x -= y_to_power

        quotient += (1 << power_of_two)

    return quotient

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
