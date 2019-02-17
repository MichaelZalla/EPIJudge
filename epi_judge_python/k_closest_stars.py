import functools
import math
import itertools
import heapq
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:

    max_heap, stars_iter = [], iter(stars)

    for star in itertools.islice(stars_iter, k):
        heapq.heappush(max_heap, (-star.distance, star))

    for star in stars_iter:
        heapq.heappushpop(max_heap, (-star.distance, star))

    # Note that we aren't asked to provide the k-closest in any particular order

    result = [elem[1] for elem in heapq.nsmallest(k, max_heap)]

    return result

# star1 = Star(15,24,18)
# star2 = Star(28,82,29)
# star3 = Star(18,37,85)
# star4 = Star(4,112,22)
# star5 = Star(69,21,58)

# stars = [star1,star2,star3,star4,star5]

# for index, star in enumerate(stars):
#     print(index, star.distance)

# print(find_closest_k_stars(stars, 3))

# exit()


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
