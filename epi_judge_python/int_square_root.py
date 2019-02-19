from test_framework import generic_test

# As we advance linearly through integer candidates, we know that their square
# increases exponentially!

# When we pick a candidate whose square is too large, we search the left
# subgroup of remaining candidates;

# When we pick a candidate whose square is too small, we search the right
# subgroup of remaining candidates;

# We can't simply jump to the positional mid, as this would increase or decrease
# our future squares according to an exponential scale, not a linear scale;
# thus, we would not get halfway closer to our answer;

# We have a perfect square when math.log(x, candidate) == 2; the closest
# candidate is the candidate for which math.log(x, candidate) is closest to >2;

# If c**c = x, can c even be equal to or greater than x/2?

# x=0, c=0
# x=1, c=1
# x=2, c=1
# x=3, c=1
# x=4, c=2
# x=5, c=2
# x=6, c=2
# x=8, c=2
# x=9, c=3

import math

def square_root(k: int) -> int:

    def get_closest_perfect_square(k, lower, upper):

        while lower < upper:

            lower_lgk = math.log(lower, k)
            upper_lgk = math.log(upper, k)
            mid_lgk = lower_lgk + (upper_lgk-lower_lgk)/2

            mid = math.ceil(math.pow(k, mid_lgk))
            mid_squared = mid**2

            if mid_squared <= k:
                lower = mid
            else:
                upper = mid-1

            # print(f'Now searching range {lower}, {upper} (size: {upper-lower})')

        return lower

    # print(f'Finding closest integer square root of {k}')

    if k == 0:
        return 0

    return get_closest_perfect_square(k, 1, math.ceil(k/2))

# print(0, square_root(0))
# print(1, square_root(1))
# print(2, square_root(2))
# print(3, square_root(3))
# print(4, square_root(4))
# print(5, square_root(5))
# print(6, square_root(6))
# print(7, square_root(7))
# print(8, square_root(8))
# print(9, square_root(9))

# print(9604, square_root(9604))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
