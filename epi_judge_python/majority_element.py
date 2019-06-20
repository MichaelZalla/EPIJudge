from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:

    candidate, count = None, 0

    for item in stream:

        if count == 0:
            candidate, count = item, 1
        elif item == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# print(majority_search(['b','a','c','a','a','b','a','a','c','a']))
# print(majority_search(['b','c','b','c','a','a','a','a','a','a']))
# print(majority_search(['a','a','a','a','a','a','b','c','b','c']))

# exit()

def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
