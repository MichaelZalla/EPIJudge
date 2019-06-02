from typing import List

from test_framework import generic_test, test_utils

import math


def generate_balanced_parentheses(n: int) -> List[str]:

    def generate_parentheses(left_budget, right_budget, prefix, result = []):

        # Note that the prefix string is passed by value in each recursive call

        # If we can still 'open'...

        if left_budget:
            generate_parentheses(left_budget - 1, right_budget, prefix + '(')

        # If there is at least one unterminated 'pair' in our prefix string...

        if left_budget < right_budget:
            generate_parentheses(left_budget, right_budget - 1, prefix + ')')

        # If we've correctly used up our right parentheses, then we can safely
        # assume that the original number of pairs is now present in the prefix
        # string;

        if not right_budget:
            result.append(prefix)

        return result

    return generate_parentheses(n, n, '')


# print('n=0: ', generate_balanced_parentheses(0), end='\n\n')
# print('n=1: ', generate_balanced_parentheses(1), end='\n\n')
# print('n=2: ', generate_balanced_parentheses(2), end='\n\n')
# print('n=3: ', generate_balanced_parentheses(3), end='\n\n')
# print('n=4: ', generate_balanced_parentheses(4), end='\n\n')
# print('n=5: ', generate_balanced_parentheses(5), end='\n\n')

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
