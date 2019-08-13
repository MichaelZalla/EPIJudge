import functools

from test_framework import generic_test

BASE = 26

def get_base26_digit(c):

    return ord(c) - ord('A') + 1

def ss_decode_col_id(col: str) -> int:

    n = len(col)

    return functools.reduce(
        lambda sum, index: sum + get_base26_digit(col[n - 1 - index]) * (BASE**index),
        list(range(len(col))),
        0
    )


# print('A', ss_decode_col_id('A'))
# print('B', ss_decode_col_id('B'))
# print('C', ss_decode_col_id('C'))
# print('Z', ss_decode_col_id('Z'))
# print('AA', ss_decode_col_id('AA'))
# print('AB', ss_decode_col_id('AB'))
# print('AC', ss_decode_col_id('AC'))
# print('YY', ss_decode_col_id('YY'))
# print('ZZ', ss_decode_col_id('ZZ'))
# print('AAA', ss_decode_col_id('AAA'))
# print('AAB', ss_decode_col_id('AAB'))
# print('AAC', ss_decode_col_id('AAC'))
# print('BBB', ss_decode_col_id('BBB'))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
