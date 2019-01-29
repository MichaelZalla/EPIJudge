from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    # Checks invalid inputs and cases where reversal is trivially satisfied

    if start < 1 or finish < 1 or start == finish:
        return L

    # Advance 'origin' to node at L[start - 1]; note that origin may still be L
    # If start is 1, then origin will be positioned at L[start]

    origin = L

    for i in range(start - 2):
        origin = origin.next

    # Traverse forward (finish - start) times, setting the 'next' pointers backwards

    left = origin if start == 1 else origin.next

    next = left.next

    for i in range(finish - start):

        behind = left
        left = next
        next = next.next

        # Updates 'next' pointer to previous node

        left.next = behind

    if start == 1:

        # If the list head is the sublist's new tail, we fix up the tail to
        # point to 'None' and return the head node (left)

        origin.next = next

        return left

    else:

        # Otherwise, fix up the tail-end of the sublist to point to the
        # remainder of the linked list, and return L (which may be origin)

        origin.next.next = next
        origin.next = left

        return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
