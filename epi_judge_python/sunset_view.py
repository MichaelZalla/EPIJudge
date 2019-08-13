from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(buildings: Iterator[int]) -> List[int]:

    stack = []

    for index, height in enumerate(buildings):

        while stack and buildings[stack[-1]] <= height:
            stack.pop()

        stack.append(index)

    return list(reversed(stack))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
