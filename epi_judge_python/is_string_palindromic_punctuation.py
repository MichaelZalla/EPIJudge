from test_framework import generic_test

def is_palindrome(S: str) -> bool:

    left, right = 0, len(S) - 1

    while right > left:

        # Advance left and right positions

        while left < right and not S[left].isalnum():
            left += 1

        while right > left and not S[right].isalnum():
            right -= 1

        # Compare alphanumeric values

        if S[left].lower() != S[right].lower():
            return False

        # Advance again

        left += 1
        right -= 1

    # Assume palindromicity

    return True

# print(is_palindrome('A man, a plan, a canal, Panama.'))
# print(is_palindrome('Ray a Ray'))
# print(is_palindrome('Able was I, ere I saw Elba!'))
# print(is_palindrome('Not a palindrome.'))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
