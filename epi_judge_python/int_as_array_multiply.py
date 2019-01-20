from typing import List

from test_framework import generic_test

def add(A1, A2):

    sum, carry = [], 0

    while A1 or A2:

        digit_sum = carry

        if A1:
            digit_sum += A1.pop()
        if A2:
            digit_sum += A2.pop()

        if digit_sum <= 9:
            carry = 0
        else:
            carry = 1

        sum.append(digit_sum % 10)

    if carry:

        sum.append(carry)

    sum.reverse()

    return sum

def multiply_by_digit(A, d):

    if d == 0:

        return [0]

    product, carry = [], 0

    while A:

        digit_product = d * A.pop() + carry

        if digit_product <= 9:
            carry = 0
        else:
            carry = digit_product // 10

        product.append(digit_product % 10)

    if carry:

        product.append(carry)

    product.reverse()

    return product

def multiply_with_add(A1: List[int], A2: List[int]) -> List[int]:

    sum, places, negate = [0], 0, False

    # Determine the sign of our product

    if A1[0] < 0:
        negate = not negate
        A1[0] = abs(A1[0])

    if A2[0] < 0:
        negate = not negate
        A2[0] = abs(A2[0])

    # Consume one digit d of A2 at a time, computing the product A1 * d
    # Add product*10**places to our running sum

    while A2:

        digit = A2.pop()

        product = multiply_by_digit(A1[:], digit)

        if product != [0]:

            sum = add(sum, product + [0] * places)

        places += 1

    # Set the sign of our resulting product array

    if negate:
        sum[0] = -1 * sum[0]

    return sum

def multiply_in_place(A1: List[int], A2: List[int]) -> List[int]:

    # Determine the sign of the product

    sign = -1 if (A1[0] < 0) ^ (A2[0] < 0) else 1

    A1[0], A2[0] = abs(A1[0]), abs(A2[0])

    # The product will use at most n + m digits (places) (preallocate size)

    result = [0] * (len(A1) + len(A2))

    for i in reversed(range(len(A1))):

        for j in reversed(range(len(A2))):

            result[i + j + 1] += A1[i] * A2[j]

            # Perform a carry if necessary

            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Strips any leading zero entries from result

    first_significant_index = next(
        (index for index, digit in enumerate(result) if digit != 0),
        len(result) # default value for generator
    )

    result = result[first_significant_index:] or [0]

    return [sign * result[0]] + result[1:]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply_with_add))
