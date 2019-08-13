from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:

    words, min_distance = {}, -1

    for index, word in enumerate(paragraph):

        if word not in words:
            words[word] = (index, len(paragraph))

        else:

            prev_distance = words[word][1]
            curr_distance = index - words[word][0]

            words[word] = (index, min(prev_distance, curr_distance))

            min_distance = curr_distance if min_distance == -1 else \
                min(min_distance, curr_distance)

    return min_distance




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
