import functools
from typing import List
import collections

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)


def eliminate_duplicate(names: List[Name]) -> None:

    seen, queue = {}, collections.deque()

    for index, name in enumerate(names):

        if not (name.first_name in seen):

            # If we haven't see this name before, mark it as seen;

            seen[name.first_name] = True

            # Check whether there is a hole before this index that we can swap
            # this element to; once the unique element has been swapped, add its
            # original position to our queue of holes to fill;

            if queue:
                names[queue.pop()] = names[index]
                queue.appendleft(index)

        else:

            # We've already seen this name, so add this index to our queue;

            queue.appendleft(index)

    # Trim the list of any unfilled holes before returning;

    while(queue and queue.pop()):
        names.pop()

    return


# names1 = []
# names2 = [Name('Jack', 'Holder'), Name('Jack', 'Frost'), Name('Jack', 'DeNimble'), Name('Jack', 'DeQuick')]
# names3 = [Name('Jack', 'Holder'), Name('Jack', 'Frost'), Name('Jackie', 'Kennedy')]
# names4 = [Name('Aaron', 'Stone'), Name('Bernie', 'Rogers'), Name('Chester', 'Fuzz')]
# names5 = [Name('Aaron', 'Stone'), Name('Aaron', 'Rodriguez'), Name('Bernie', 'Rogers'), Name('Chester', 'Fuzz')]

# print(eliminate_duplicate(names1))
# print(eliminate_duplicate(names2))
# print(eliminate_duplicate(names3))
# print(eliminate_duplicate(names4))
# print(eliminate_duplicate(names5))

# exit()

@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
