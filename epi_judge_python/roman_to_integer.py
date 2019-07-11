from test_framework import generic_test

import functools

TOKEN_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def roman_to_integer(S: str) -> int:

    sum, partial = 0, 0

    for index in range(len(S) - 1):

        current = TOKEN_VALUES[S[index]]

        next = TOKEN_VALUES[S[index + 1]]

        partial += current

        if current > next:
            sum += partial
            partial = 0
        elif current < next:
            sum -= partial
            partial = 0

    sum += partial + TOKEN_VALUES[S[-1]]

    return sum

# # 1
# print('I', roman_to_integer('I'))

# # 2
# print('II', roman_to_integer('II'))

# # 9
# print('IX', roman_to_integer('IX'))

# # 11
# print('XI', roman_to_integer('XI'))

# # 59
# print('LIX', roman_to_integer('LIX'))

# # 30
# print('XXL', roman_to_integer('XXL'))

# # 14
# print('XIV', roman_to_integer('XIV'))

# # 33
# print('XXLIIV', roman_to_integer('XXLIIV'))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
