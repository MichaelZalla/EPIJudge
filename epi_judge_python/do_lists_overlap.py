import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_cycle_length(cycle_end: ListNode) -> int:

    start, steps = cycle_end, 0

    while True:

        start = start.next
        steps += 1

        if start is cycle_end:
            return steps

def get_cycle_start(L: ListNode, cycle_length: int) -> ListNode:

    behind = ahead = L

    for _ in range(cycle_length):
        ahead = ahead.next

    while behind is not ahead:
        behind, ahead = behind.next, ahead.next

    return behind

def has_cycle(L: ListNode) -> bool:

    fast = slow = L

    while fast and fast.next and fast.next.next:

        slow, fast = slow.next, fast.next.next

        if slow is fast:

            cycle_length = get_cycle_length(slow)

            return get_cycle_start(L, cycle_length)

    return None

def distance(node1: ListNode, node2: ListNode) -> int:

    distance = 0

    while node1 is not node2:
        node1 = node1.next
        distance += 1

    return distance

def get_overlapping_node_in_lists_nocycle(L1: ListNode,
                                            L2: ListNode) -> Optional[ListNode]:

    def get_list_length(L):

        length = 1

        while L:
            L = L.next
            length += 1

        return length

    L1_len, L2_len = get_list_length(L1), get_list_length(L2)

    # Have L2 reference the longer lists, and L1 reference the shorter list;

    if L1_len > L2_len:
        L1, L2 = L2, L1

    delta = abs(L1_len - L2_len)

    for _ in range(delta):
        L2 = L2.next

    # Walk up both lists from their (n-delta)-th nodes, checking for overlap;

    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next

    return L1 or None

def get_overlapping_node_in_lists_cycle(L1: ListNode,
                                            L2: ListNode) -> Optional[ListNode]:

    root1, root2 = has_cycle(L1), has_cycle(L2)

    # If neither list has a cycle, check whether the lists overlap;

    if not root1 and not root2:
        return get_overlapping_node_in_lists_nocycle(L1, L2)

    # Else, if only one list contains a cycle, we know that the two lists
    # cannot overlap;

    elif (root1 and not root2) or (root2 and not root1):
        return None

    # Else, both lists must contain a cycle; we need to determine whether the
    # two cycles overlap, in which case the two lists overlap;

    # Traverse one of the 2 cycles, checking for overlap with the other cycle;

    temp = root1

    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break

    if temp is not root2:

        # The 2 cycles are disjoint; thus, these lists do not overlap;
        return None

    # Find the first node in L1 and L2 and overlaps; does this node occur before
    # the overlapping cycle, or is the node part of that cycle?

    stem1_len, stem2_len = distance(L1, root1), distance(L2, root2)

    if stem1_len > stem2_len:
        L1, L2 = L2, L1
        root1, root2 = root2, root1

    # Walk up the list that holds the most nodes between its list head and the
    # start of its respective cycle;

    for _ in range(abs(stem1_len - stem2_len)):
        L2 = L2.next

    # Traverses the last n nodes in each list's 'stem', approaching the start of
    # each list's respective cycle;

    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next

    # At this point, either L1 or L2 points to (a) the start of the list's
    # cycle, or (b) the first overlapping node between the two lists;

    # Either the overlapping node is before the cycle, or part of the cycle;

    if L1 is L2:

        # Lists overlap before the cycle;
        return L1

    else:

        # Lists overlap within the cycle; we can return any node in the cycle;
        return root1


# L1_a = ListNode(1, None)
# L1_b = ListNode(2, None)

# L2_a = ListNode(3, None)
# L2_b = ListNode(4, None)
# L2_c = ListNode(5, None)
# L2_d = ListNode(6, None)

# L1_a.next = L1_b
# L1_b.next = L2_b

# L2_a.next = L2_b
# L2_b.next = L2_c
# L2_c.next = L2_d
# L2_d.next = L2_a

# print(get_overlapping_node_in_lists_cycle(L1_a, L2_a))

# exit()


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(get_overlapping_node_in_lists_cycle, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
