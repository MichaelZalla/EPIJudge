import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def intersects(R1: Rect, R2: Rect) -> Rect:

    return (
        R1.x <= (R2.x + R2.width) and
        (R1.x + R1.width) >= R2.x and
        (R1.y) <= (R2.y + R2.height) and
        (R1.y + R1.height) >= R2.y
    )

def intersect_rectangle(R1: Rect, R2: Rect) -> Rect:

    if intersects(R1, R2):

        return Rect(
            max(R1.x, R2.x),
            max(R1.y, R2.y),
            min((R1.x + R1.width), (R2.x + R2.width)) - max(R1.x, R2.x),
            min((R1.y + R1.height), (R2.y + R2.height)) - max(R1.y, R2.y)
        )

    else:

        return Rect(0, 0, -1, -1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
