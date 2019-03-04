from test_framework import generic_test

import collections

def is_letter_constructible_from_magazine_iterletter(letter_text: str,
                                          magazine_text: str) -> bool:

    mag_counts = collections.Counter(magazine_text)

    letter_counts = collections.Counter(letter_text)

    # Assert that we're dealing with a subset of magazine characters

    if not (set(letter_counts.keys()) <= set(mag_counts.keys())):
        return False

    # Assert that the letter doesn't require more of one letter than is available

    for char, count  in letter_counts.items():
        if mag_counts[char] < count:
            return False

    return True

def is_letter_constructible_from_magazine_itermag(letter_text: str,
                                          magazine_text: str) -> bool:

    letter_counts = collections.Counter(letter_text)

    for c in mag_text:

        if c in letter_counts:
            letter_counts[c] -= 1

            if letter_counts[c] == 0:
                del letter_counts[c]

                if not letter_counts:
                    return True

    return not letter_counts


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine_iterletter))
