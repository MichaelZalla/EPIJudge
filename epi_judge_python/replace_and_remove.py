import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# @NOTE(mzalla) Since Python uses the C runtime stack, deep recursion in Python
# can cause the C stack to overflow, resulting in a memory access violator
# (segfault); the recursive solution isn't adequate for very large S inputs
#
# See: https://stackoverflow.com/a/19179377

def replace_and_remove_recursive(k: int, S: List[str], pos:int=0) -> int:

    if k == 0:
        return pos

    char = S[pos]

    if char == '':
        return pos

    elif char != 'a' and char != 'b':

        return replace_and_remove_recursive(k, S, pos+1)

    elif char == 'b':

        next_taken = pos+1

        while next_taken < len(S) and (S[next_taken] == 'b' or S[next_taken] == ''):
            next_taken += 1

        if next_taken == len(S):
            S[pos] = ''

        else:
            S[pos], S[next_taken] = S[next_taken], S[pos]

        return replace_and_remove_recursive(k-1, S, pos)

    elif char == 'a':

        next_free = pos+1

        while S[next_free] != 'b' and S[next_free] != '':
            next_free += 1

        for j in reversed(range(pos + 1, next_free)):
            S[j], S[j+1] = S[j+1], S[j]

        S[pos] = S[pos+1] = 'd'

        return replace_and_remove_recursive(k-1, S, pos+2)

def replace_and_remove_iterative(k: int, S: List[str]) -> int:

    pos = 0

    while k > 0:

        char = S[pos]

        if char == '':
            break

        elif char != 'a' and char != 'b':
            pos += 1

        elif char == 'b':

            next_taken = pos+1

            while next_taken < len(S) and (S[next_taken] == 'b' or S[next_taken] == ''):
                next_taken += 1

            if next_taken == len(S):
                S[pos] = ''

            else:
                S[pos], S[next_taken] = S[next_taken], S[pos]

            k -= 1

        elif char == 'a':

            next_free = pos+1

            while S[next_free] != 'b' and S[next_free] != '':
                next_free += 1

            for j in reversed(range(pos + 1, next_free)):
                S[j], S[j+1] = S[j+1], S[j]

            S[pos] = S[pos+1] = 'd'

            pos += 2
            k -= 1

    return pos

def replace_and_remove_linear(k: int, S: List[str]) -> int:

    write_index, a_count = 0, 0

    for i in range(k):

        if S[i] != 'b':
            S[write_index] = S[i]
            write_index += 1
        if S[i] == 'a':
            a_count += 1

    current_index = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1

    while current_index >= 0:

        if S[current_index] == 'a':
            S[write_index-1:write_index+1] = 'dd'
            write_index -= 2
        else:
            S[write_index] = S[current_index]
            write_index -= 1

        current_index -= 1

    return final_size


# print('1. ', replace_and_remove_iterative(1, ['']))
# print('2. ', replace_and_remove_iterative(2, ['','']))
# print('3. ', replace_and_remove_iterative(1, ['c']))
# print('4. ', replace_and_remove_iterative(1, ['b']))
# print('5. ', replace_and_remove_iterative(2, ['b','b']))
# print('6. ', replace_and_remove_iterative(1, ['a','']))
# print('7. ', replace_and_remove_iterative(2, ['a','a','','']))
# print('8. ', replace_and_remove_iterative(2, ['a','a','b','']))

# exit()


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove_linear, size, s))
    return s[:res_size]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
