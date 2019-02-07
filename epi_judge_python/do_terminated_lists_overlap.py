import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists_bruteforce(L1: ListNode, L2: ListNode) -> ListNode:

    node = L1

    if L2 is None:

        return None

    while node is not None:

        cursor = L2

        while cursor is not None:

            if cursor is node:
                return node

            cursor = cursor.next

        node = node.next

    return None

def overlapping_no_cycle_lists_zipup(L1: ListNode, L2: ListNode) -> ListNode:

    def list_length(L):

        length = 0

        while L:
            length += 1
            L = L.next

        return length

    L1_len, L2_len = list_length(L1), list_length(L2)

    min, max = L1, L2

    if L1_len > L2_len:
        min, max = L2, L1

    for i in range(abs(L1_len - L2_len)):
        max = max.next

    while min and max and min is not max:
        min, max = min.next, max.next

    # Returns common node, or None

    return min


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists_zipup, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
