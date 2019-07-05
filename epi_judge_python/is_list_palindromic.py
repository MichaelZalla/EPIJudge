from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:

    left = right = head = ListNode(None)

    head.next = L

    # Lists of length 0 or 1 are trivially palindromic

    if not head.next or not head.next.next:
        return True

    reverse_half = ListNode(None)

    while right.next and right.next.next:

        # Advance right by 2
        right = right.next.next

        # Advanced left by 1
        left = left.next

        # Add a copy of 'left' node's data to reversed list
        node = ListNode(left.data)
        node.next = reverse_half.next
        reverse_half.next = node

    # Skip over middle element in odd-length lists
    if right.next:
        left = left.next

    left = left.next

    left_mirrored_node = reverse_half.next

    while left:

        if left.data != left_mirrored_node.data:
            return False

        left = left.next
        left_mirrored_node = left_mirrored_node.next

    return True


# n0 = ListNode(0)
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(2)
# n4 = ListNode(1)
# n5 = ListNode(0)

# n0.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = None

# print(is_linked_list_a_palindrome(n0))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
