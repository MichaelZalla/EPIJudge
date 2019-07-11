from test_framework import generic_test


def snake_string(S: str) -> str:

    return ''.join(
        [S[i] for i in range(1, len(S), 4)] +
        [S[i] for i in range(0, len(S), 2)] +
        [S[i] for i in range(3, len(S), 4)]
    )

def snake_string_pythonic(S):

    return S[1::4] + S[::2] + S[3::4]

# print(snake_string('Hello World!'))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string_pythonic))
