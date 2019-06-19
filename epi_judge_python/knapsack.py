import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], max_weight: int) -> int:

    memo = [[-1] * (max_weight + 1) for _ in items]

    for item_index, item in enumerate(items):

        for weight in range(0, max_weight + 1):

            # Only one item may be stolen (once) from a single-item set...

            if item_index == 0:

                memo[item_index][weight] = 0 if item.weight > weight else item.value

            # If we can't even choose this item...

            elif item.weight > weight:

                memo[item_index][weight] = memo[item_index - 1][weight]

            # Otherwise, if we have the option to choose this item...

            else:

                memo[item_index][weight] = max(
                    memo[item_index - 1][weight],
                    memo[item_index - 1][weight - item.weight] + item.value
                )

    return memo[-1][-1]

def optimum_subject_to_capacity_recursive(items: List[Item], max_weight: int) -> int:

    def optimum_subject_to_capacity(k: int, available_weight: int):

        if k < 0:
            return 0

        if V[k][available_weight] == -1:

            without_current_item = optimum_subject_to_capacity(k - 1, available_weight)

            with_current_item = (
                0 if available_weight < items[k].weight else
                items[k].value + optimum_subject_to_capacity(k - 1, available_weight - items[k].weight))

            V[k][available_weight] = max(
                without_current_item,
                with_current_item
            )

        return V[k][available_weight]

    V = [[-1] * (max_weight + 1) for _ in items]

    return optimum_subject_to_capacity(len(items) - 1, max_weight)


# items = [
#     Item(weight=2, value=1),
#     Item(weight=4, value=3),
#     Item(weight=5, value=10),
#     Item(weight=7, value=9),
#     Item(weight=8, value=14),
# ]

# print(optimum_subject_to_capacity(items, 0))
# print(optimum_subject_to_capacity(items, 1))
# print(optimum_subject_to_capacity(items, 2))
# print(optimum_subject_to_capacity(items, 3))
# print(optimum_subject_to_capacity(items, 4))
# print(optimum_subject_to_capacity(items, 5))
# print(optimum_subject_to_capacity(items, 6))
# print(optimum_subject_to_capacity(items, 7))
# print(optimum_subject_to_capacity(items, 8))

# exit()

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
