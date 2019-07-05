from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_data: List[int]) -> Optional[BstNode]:

    if not preorder_data:
        return None

    indices = (i for i, code in enumerate(preorder_data) if code > preorder_data[0])

    default_value = len(preorder_data)

    iterator = next(indices, default_value)

    return BstNode(
        preorder_data[0],
        rebuild_bst_from_preorder(preorder_data[1:iterator]),
        rebuild_bst_from_preorder(preorder_data[iterator:])
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
