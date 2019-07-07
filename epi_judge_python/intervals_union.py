import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

def get_left_endpoint(interval):

    # Returns a tuple representing the left endpoint, for sorting purposes;

    return (interval.left.val, 0 if interval.left.is_closed else 1)

def overlaps(A, B):

    # If one interval starts after the other ends, then there can be no overlap;

    if A.left.val > B.right.val or B.left.val > A.right.val:
        return False

    # Otherwise, if one interval starts where the other ends, but both interval
    # endpoints are not closed, then these intervals do not overlap;

    elif A.left.val == B.right.val and not A.left.is_closed and not B.right.is_closed:
        return False
    elif B.left.val == A.right.val and not B.left.is_closed and not A.right.is_closed:
        return False

    # Otherwise, these two intervals must overlap

    else:
        return True

def union_of_intervals(intervals: List[Interval]) -> List[Interval]:

    # Sorts intervals by their left endpoints

    intervals.sort(key=get_left_endpoint)

    union_set, index = [], 0

    # While there are still unvisited intervals in our list...

    while index < len(intervals):

        # Start interval must be the starting point of our current union

        start_interval = end_interval = intervals[index]

        # While some interval follows that overlaps with our current window...

        while index < len(intervals) - 1 and overlaps(intervals[index + 1], end_interval):

            next_interval = intervals[index + 1]

            # Can we extend our current end_interval to be next_interval?

            if next_interval.right.val > end_interval.right.val or \
                (next_interval.right.val == end_interval.right.val and next_interval.right.is_closed):

                end_interval = next_interval

            index += 1

        # At this point, (start_interval, end_interval) forms our union

        union_set.append(Interval(left=start_interval.left, right=end_interval.right))

        index += 1

    return union_set


# print(union_of_intervals([
#     Interval(left=Endpoint(val=9, is_closed=False), right=Endpoint(val=11, is_closed=True)),
#     Interval(left=Endpoint(val=7, is_closed=True), right=Endpoint(val=8, is_closed=False)),
#     Interval(left=Endpoint(val=5, is_closed=True), right=Endpoint(val=7, is_closed=False)),
#     Interval(left=Endpoint(val=3, is_closed=True), right=Endpoint(val=4, is_closed=False)),
#     Interval(left=Endpoint(val=2, is_closed=True), right=Endpoint(val=4, is_closed=True)),
#     Interval(left=Endpoint(val=8, is_closed=True), right=Endpoint(val=11, is_closed=False)),
#     Interval(left=Endpoint(val=1, is_closed=True), right=Endpoint(val=1, is_closed=True)),
#     Interval(left=Endpoint(val=0, is_closed=False), right=Endpoint(val=3, is_closed=False)),
# ]))

# exit()


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
