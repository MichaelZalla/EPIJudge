from typing import Optional

from list_node import ListNode
from test_framework import generic_test

from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last_doublereverse(L: ListNode, k: int) -> Optional[ListNode]:

    def reverse_list(L):

        if L is None:
            return L

        next, L.next = L.next, None

        while next:
            temp = next.next
            next.next = L
            L = next
            next = temp

        return L

    reverse_L = reverse_list(L)

    count, node = 1, reverse_L

    if k is 1:
        return reverse_list(node.next)

    while node:

        if count is k-1:
            node.next = node.next.next
            break

        node = node.next

        count += 1

    return reverse_list(reverse_L)

def remove_kth_last_scoutahead(L: ListNode, k: int) -> Optional[ListNode]:

    sentry_head = ListNode(0, L)

    first = sentry_head.next

    for _ in range(k):
        first = first.next

    second = sentry_head

    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return sentry_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last_scoutahead))
