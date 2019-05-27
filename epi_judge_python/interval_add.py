import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def overlaps(interval1, interval2):
    return (interval1.left <= interval2.right and interval1.right >= interval2.left)

def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:

    overlapping = [interval for interval in disjoint_intervals if overlaps(interval, new_interval)]

    overlapping.append(new_interval)

    start = min([interval.left for interval in overlapping])
    finish = max([interval.right for interval in overlapping])

    # start = min(list(map(lambda x: x.left, overlapping)))
    # finish = max(list(map(lambda x: x.right, overlapping)))

    return \
        [interval for interval in disjoint_intervals if interval.right < start] + \
        [Interval(start, finish)] +\
        [interval for interval in disjoint_intervals if interval.left > finish]

# I0 = []
# E0 = Interval(4,8)

# I1 = [Interval(1,2), Interval(3,4), Interval(6,7)]
# E1 = Interval(4,8)

# print(add_interval(I0, E0))
# print(add_interval(I1, E1))

# exit()

@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
