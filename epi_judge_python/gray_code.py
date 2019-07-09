import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def gray_code(k: int) -> List[int]:

    def gray_code_int_helper(k, prev_code = [0,1]):

        if k == 1:
            return prev_code

        return gray_code_int_helper(
            k - 1,
            prev_code + [digit | (1 << k-1) for digit in prev_code[::-1]]
        )

    def gray_code_string_helper(k, prev_code = ['0','1']):

        if k == 1:
            return [int(code, 2) for code in prev_code]

        new_code = ['0' + token for token in prev_code]
        new_code += ['1' + token for token in prev_code[::-1]]

        return gray_code_string_helper(k - 1, new_code)

    if k == 0:
        return [0]

    return gray_code_int_helper(k)

# print(["{0:b}".format(code).zfill(1) for code in gray_code(1)])
# print(["{0:b}".format(code).zfill(2) for code in gray_code(2)])
# print(["{0:b}".format(code).zfill(3) for code in gray_code(3)])
# print(["{0:b}".format(code).zfill(4) for code in gray_code(4)])
# print(["{0:b}".format(code).zfill(5) for code in gray_code(5)])

# exit()


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure('Length mismatch: expected ' + str(expected_size) +
                          ', got ' + str(len(result)))
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure('Two adjacent entries are equal')
            else:
                raise TestFailure(
                    'Two adjacent entries differ by more than 1 bit')

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure('Not all entries are distinct: found ' +
                          str(len(result) - len(uniq)) + ' duplicates')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('gray_code.py', 'gray_code.tsv',
                                       gray_code_wrapper))
