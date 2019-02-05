from test_framework import generic_test

TAGS = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def is_well_formed(S: str) -> bool:

    opening = []

    for token in S:

        if token in TAGS:
            opening.append(token)
        elif not opening or token != TAGS[opening.pop()]:
            return False

    return not opening



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
