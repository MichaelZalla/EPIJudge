from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode


def stable_sort_list_naive(L: ListNode) -> Optional[ListNode]:

    if not L or not L.next:
        return L

    node, min_value = L, L.data

    while node:
        min_value = min(min_value, node.data)
        node = node.next

    sorted_head = sorted_tail = ListNode(data=None, next=L)

    unsorted_head = sorted_tail.next

    while sorted_tail.next:

        # Consume any minimum-value nodes at the front of unsorted

        while sorted_tail.next and sorted_tail.next.data == min_value:
            sorted_tail = sorted_tail.next
            unsorted_head = unsorted_head.next

        # If we ended up consuming all remaining unsorted nodes, return sorted

        if not sorted_tail.next:
            return sorted_head.next

        # Otherwise, we'll walk through the remaining unsorted nodes (again)

        prev = sorted_tail
        node = sorted_tail.next
        new_min_value = node.data

        while node:

            if node.data == min_value:

                # Move node to after sorted and before unsorted

                prev.next = node.next
                node.next = unsorted_head

                sorted_tail.next = node
                sorted_tail = node

                node = prev.next

            else:

                new_min_value = min(new_min_value, node.data)

                prev, node = node, node.next

        # Update new minimum value for next pass through unsorted

        min_value = new_min_value

    return sorted_head.next


def merge_two_sorted_lists(L1, L2):

    # Edge cases where one list is empty

    if not L1:
        return L2

    if not L2:
        return L1

    next, max, head = L1, L2, None

    # When one list is entirely consumed, the other need not be modified

    while next and max:

        # Determine min and max for this iteration

        min = next if next.data <= max.data else max
        max = max if min == next else next

        # Remeber to update next after updating min

        next = min.next

        # Set head to initial min (only assigns once)

        if head is None:
            head = min

        # Advance min forward as far as possible (updating next to be ahead)

        while min.next and min.next.data <= max.data:
            min, next = min.next, min.next.next

        # Update min node to point to max

        min.next = max

    return head

def stable_sort_list_mergesort(L: ListNode) -> Optional[ListNode]:

    # Checks our 2 base cases

    if not L or not L.next:
        return L

    # Otherwise, we'll need to recurse; split L into 2 sublists;

    pre_slow, slow, fast = None, L, L

    while fast and fast.next:
        pre_slow = slow
        slow, fast = slow.next, fast.next.next

    # At this point, we have two lists of equal-ish size:
    #
    # 1. [L -> ... -> pre_slow]
    # 2. [slow -> ... -> fast]

    # Severs L into two sublists

    pre_slow.next = None

    # Recurse on both sublists, returning the sorted sublists

    left_sorted = stable_sort_list_mergesort(L)
    right_sorted = stable_sort_list_mergesort(slow)

    # Merge the two sublists

    return merge_two_sorted_lists(left_sorted, right_sorted)


# n0 = ListNode(-4)
# n1 = ListNode(2)
# n2 = ListNode(0)
# n3 = ListNode(5)
# n4 = ListNode(-4)
# n5 = ListNode(5)
# n6 = ListNode(2)
# n7 = ListNode(1)
# n8 = ListNode(-1)
# n9 = ListNode(3)

# n0.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8
# n8.next = n9
# n9.next = None

# print(stable_sort_list_mergesort(n0))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list_mergesort))
