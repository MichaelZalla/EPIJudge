import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city_naive(gallons: List[int], distances: List[int]) -> int:

    # Given a start city, end city, and a starting fuel tank, determine whether
    # the end city is reachable from the start city, passing through all
    # cities between them, in order;

    def reachable(i, j, tank):

        # Positive base case: A city reaches itself, trivially

        if i == j:
            return True

        # Determine net affect on our tank by passing through this city;

        new_tank = tank + gallons[i] - distances[i] / MPG

        # Negative base case: we're stranded on the highway!

        if new_tank < 0:
            return False

        # Recurrence relation for reachability

        return reachable((i + 1) % len(gallons), j, new_tank)

    # For each city, as an origin, check whether a round trip is possible;

    for start_city in range(len(gallons)):

        starting_tank = gallons[start_city] - distances[start_city] / MPG

        # By visiting the next city, could we get back to where we started?

        i, j = (start_city + 1) % len(gallons), start_city,

        if starting_tank >= 0 and reachable(i, j, starting_tank):
            return start_city


def find_ample_city_heuristic(gallons, distances):

    starting_tank, min_starting_index, min_starting_tank = 0, 0, 0

    for city_index in range(1, len(gallons)):

        starting_tank += \
            (gallons[city_index - 1] - distances[city_index - 1] / MPG)

        if starting_tank < min_starting_tank:
            min_starting_tank, min_starting_index = starting_tank, city_index

    return min_starting_index


# print(find_ample_city_heuristic(
#     [0],
#     [0]
# ))

# print(find_ample_city_heuristic(
#     [0, 100],
#     [10,50]
# ))

# print(find_ample_city_heuristic(
#     [0, 100, 5],
#     [10,50, 900]
# ))

# print(find_ample_city_heuristic(
#     [30, 25, 10, 10, 50, 20, 5  ],
#     [400,600,200,100,900,600,200]
# ))

# exit()

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city_heuristic, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
