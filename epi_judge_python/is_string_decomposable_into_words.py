import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(s: str, D: Set[str]) -> List[str]:

    # def decompose_into_words_naive(s: str, D: Set[str]) -> List[str]:

    #     if not s:
    #         return []

    #     if s in memo:
    #         return memo[s]

    #     # Try with leading words in dictionary

    #     i = 0

    #     while i < len(s):

    #         prepend = s[0:i]

    #         if prepend in D:

    #             for j in range(len(s) - 1, i - 1, -1):

    #                 append = s[j:]

    #                 if append in D:

    #                     remainder = s[i:j]

    #                     decompose_remainder = decompose_into_words_naive(remainder, D)

    #                     if decompose_remainder is not False:
    #                         memo[s] = [prepend] + decompose_remainder + [append]
    #                         return memo[s]

    #         i += 1

    #     return False

    def decompose_into_words(s: str, D: Set[str]) -> List[str]:

        word_length = [-1] * len(s)

        for i in range(len(s)):

            if s[:i+1] in D:
                word_length[i] = i + 1

            if word_length[i] == -1:

                for j in range(i):

                    if word_length[j] != -1 and s[j+1:i+1] in D:
                        word_length[i] = i - j
                        break

        words = []

        if s and word_length[-1] != -1:

            i = len(s) - 1

            while i > -1:

                prev_word = s[i + 1 - word_length[i]:i + 1]

                words.append(prev_word)

                i -= word_length[i]

            words.reverse()

        return words

    # memo = {}

    # for word in D:
    #     memo[word] = [word]

    return decompose_into_words(s, D)


# dictionary = {'bed', 'bath', 'hand', 'and', 'beyond'}

# print(decompose_into_dictionary_words('', dictionary))
# print(decompose_into_dictionary_words('bed', dictionary))
# print(decompose_into_dictionary_words('bedbathandbeyond', dictionary))
# print(decompose_into_dictionary_words('bedbathandbey', dictionary))
# print(decompose_into_dictionary_words('edbathandbeyond', dictionary))

# exit()


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
