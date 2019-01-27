from typing import Optional

from list_node import ListNode
from test_framework import generic_test

class LinkedNode:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

    def __repr__(self):

        chars, node = [], self

        while node:

            chars.append(str(node.data))

            if node.next:
                chars.append(' -> ')

            node = node.next

        return ''.join(chars)

def make_linked_list(values):

    if len(values) == 0:
        return None

    head = cursor = LinkedNode(values[0])

    for i in range(1, len(values)):
        cursor.next = LinkedNode(values[i], None)
        cursor = cursor.next

    return head

def merge_two_sorted_lists(
    L1: Optional[ListNode],
    L2: Optional[ListNode]) -> Optional[ListNode]:

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


# L1 = make_linked_list([0,0,2,3])
# L2 = make_linked_list([0,1,2,5])

# L1 = make_linked_list([-14, -13, -9, -6, -5, -2, -1, 1, 4, 7, 8, 10, 12, 13])
# L2 = make_linked_list([-25, -23, -18, -18, -14, -8, -8, -6, -3, -2, -1, 2, 5, 8, 8, 8, 12, 12, 12, 14, 14, 20, 20, 22, 25, 26])

# print(merge_two_sorted_lists(L1, L2))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
