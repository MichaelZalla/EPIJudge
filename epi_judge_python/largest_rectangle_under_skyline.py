from typing import List

from test_framework import generic_test


def calculate_largest_rectangle_naive(B: List[int]) -> int:

    def get_max_run_width_for_floor(floor):

        start, max_width = 0, 0

        while start < len(B):

            while B[start] < floor:

                start += 1

                if start == len(B):
                    return max_width

            end = start

            while end < len(B) - 1 and B[end + 1] >= floor:
                end += 1

            width = end - start + 1

            if width > max_width:
                max_width = width

            start = end + 1

        return max_width

    if not B:
        return 0

    max_area, max_run_width = 0, 0

    for floor in reversed(range(1, max(B) + 1)):

        run_width = get_max_run_width_for_floor(floor)

        area = run_width * floor

        if run_width > max_run_width and area > max_area:
            max_area, max_run_width = area, run_width

    return max_area


def calculate_largest_rectangle_stack(B: List[int]) -> int:

    max_area, stack = 0, []

    for index, height in enumerate(B + [0]):

        while stack and B[stack[-1]] >= height:

            blocked_index = stack.pop()

            height_with_blocked_index_as_min = B[blocked_index]

            width_with_blocked_index_as_min = (index - stack[-1] - 1) if stack else index

            area = height_with_blocked_index_as_min * width_with_blocked_index_as_min

            if area > max_area:
                max_area = area

        stack.append(index)

    return max_area


# print(calculate_largest_rectangle_stack([1,3,2,4,2,2,4,2,1,3,4,2]))
# print(calculate_largest_rectangle_stack([1,2,2,4]))
# print(calculate_largest_rectangle_stack([1,0,1,0,1]))
# print(calculate_largest_rectangle_stack([1,2,2,1,3]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle_stack))
