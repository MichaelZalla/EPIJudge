from typing import List

from test_framework import generic_test, test_utils

M = {}

M['0'] = '0'
M['1'] = '1'
M['2'] = 'ABC'
M['3'] = 'DEF'
M['4'] = 'GHI'
M['5'] = 'JKL'
M['6'] = 'MNO'
M['7'] = 'PQRS'
M['8'] = 'TUV'
M['9'] = 'WXYZ'

def phone_mnemonic(S: str) -> List[str]:

    def add_mnemonics(S, index, partial_result):

        if index == len(S):

            results.append(''.join(partial_result))

            return

        digit = S[index]

        letters = M[digit]

        for letter in letters:

            partial_result[index] = letter

            add_mnemonics(S, index + 1, partial_result)

            # partial_result = partial_result[:-1]

    results, partial_result = [], [0] * len(S)

    add_mnemonics(S, 0, partial_result)

    return results


# print(phone_mnemonic('859'))
# print(phone_mnemonic('2276696'))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
