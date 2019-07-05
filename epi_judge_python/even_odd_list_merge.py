from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:

    if not L:
        return L

    first_odd = L.next

    current_even, current_odd = L, L.next

    while current_even and current_odd:

        if current_odd.next:

            current_even.next = current_odd.next

            if current_odd.next.next:
                current_odd.next = current_odd.next.next
            else:
                current_odd.next = None

            current_even, current_odd = current_even.next, current_odd.next

        else:

            current_even.next = first_odd
            current_even = None

    if current_even:
        current_even.next = first_odd

    return L


# n0 = ListNode(0)
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)

# n0.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = None

# print(even_odd_merge(n0))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
