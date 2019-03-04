from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s: str) -> bool:

    counts = Counter(s)

    return len(list(filter(lambda count: count % 2 == 1, counts.values()))) < 2


# s1 = 'level'
# s2 = 'rotator'
# s3 = 'foobaraboof'
# s4 = 'edified'

# print(s1, can_form_palindrome(s1))
# print(s2, can_form_palindrome(s2))
# print(s3, can_form_palindrome(s3))
# print(s4, can_form_palindrome(s4))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
