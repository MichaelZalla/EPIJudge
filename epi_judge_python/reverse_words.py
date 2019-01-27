import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words_recursive(S):

    left, right = 0, len(S) - 1

    while left < right and not chr(S[left]).isalnum():
        left += 1

    while right > left and not chr(S[right]).isalnum():
        right -= 1

    if left >= right:
        return S

    # Find word boundaries (end is first position after word)

    left_end, right_end = left + 1, right - 1

    while left_end < right and chr(S[left_end]).isalnum():
        left_end += 1

    while right_end > left and chr(S[right_end]).isalnum():
        right_end -= 1

    # Check if S contains a single word

    same_word = False

    if right_end == left: # or left_end == right:
        left_end += 1
        right_end -= 1
        same_word = True

    # Otherwise, S must contain multiple words with separator(s)

    # Extract left, middle, right, and pads before we clear S bytearray

    left_word, right_word = S[left:left_end], S[right_end+1:right+1]

    middle = reverse_words_recursive(S[left_end:right_end+1])

    left_pad, right_pad = S[:left], S[right+1:]

    # Clears the bytearray so we can replace its contents (return in-place S)

    S.clear()

    S += right_pad + right_word + ((middle + left_word) if same_word == False else middle) + left_pad

    # print(S)

    return S

def reverse_range(S, start, end):

    while start < end:
        S[start], S[end] = S[end], S[start]
        start, end = start + 1, end - 1

def reverse_words_doublepass(S):

    S.reverse()

    start = 0

    while True:

        # Reverse next word in S

        end = S.find(b' ', start)

        if end < 0:
            break

        reverse_range(S, start, end - 1)

        start = end + 1

    # Reverse last word in S

    reverse_range(S, start, len(S) - 1)

# print(reverse_words_recursive(bytearray('Alice likes Bob', 'utf-8')))
# print(reverse_words_recursive(bytearray('Hello.', 'utf-8')))
# print(reverse_words_recursive(bytearray('Hello world.', 'utf-8')))
# print(reverse_words_recursive(bytearray('Hello world, it certainly is a sunny day.', 'utf-8')))
# print(reverse_words_recursive(bytearray('Hello world, it certainly is a sunny day.', 'utf-8')))
# print(reverse_words_recursive(bytearray(' fVuWXoW  i J6bNBgS ', 'utf-8')))
# print(reverse_words_recursive(bytearray('wy8 y0N8sqBFuoq0VYWIc2xo B8yX p07 3t3PV p J6bNBgS  i fVuWXoW H6uj1m7AU aaN sBdOHmDdqE Cknw35vn WX67 sPGC', 'utf-8')))

# exit()

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words_doublepass, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
