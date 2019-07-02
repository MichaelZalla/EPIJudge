import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def get_path(M: List[List[int]], S: Coordinate,
                E: Coordinate) -> List[Coordinate]:

    def get_neighbors(coord):

        # Return all valid adjacent coordinates to the input coordinate

        x, y, n = coord.x, coord.y, []

        # Check to the left
        if x > 0 and M[x-1][y] == WHITE:
            n.append(Coordinate(x-1, y))

        # Check to the right
        if x < len(M) - 1 and M[x+1][y] == WHITE:
            n.append(Coordinate(x+1, y))

        # Check above
        if y > 0 and M[x][y-1] == WHITE:
            n.append(Coordinate(x, y-1))

        # Check below
        if y < len(M[0]) - 1 and M[x][y+1] == WHITE:
            n.append(Coordinate(x, y+1))

        return n

    # Start with S as our fronteir; mark S as visited so we don't revisit it

    frontier, visited = collections.deque([S]), {}

    visited[str(S)] = None

    while frontier:

        # Graph BFS means we need to visit least-recently-seen-first (i.e., stack)

        coord = frontier.popleft()

        # Did we reach the exit coordinate?

        if coord.x == E.x and coord.y == E.y:

            # Construct the path from S to E, using records in 'visited'

            # Note that we use collections.deque to construct the path from
            # back-to-front with O(1) additions to the front of the list;

            path, prev = collections.deque([E]), visited[str(coord)]

            while prev != S:

                path.appendleft(prev)

                prev = visited[str(prev)]

            path.appendleft(S)

            # Returns a complete path starting at S and ending at E

            return path

        # Otherwise, add this position's neighboring positions to our frontier

        neighbors = [neighbor for neighbor in get_neighbors(coord) \
            if str(neighbor) not in visited]

        for n in neighbors:

            visited[str(n)] = coord

            frontier.append(n)

    # At this point, we've exhausted our search without finding E

    return None


# M1 = [
#     [ WHITE, WHITE, WHITE ],
#     [ BLACK, WHITE, WHITE ],
#     [ WHITE, WHITE, BLACK ],
# ]

# print(get_path(M1, Coordinate(0,0), Coordinate(0,2)))

# exit()


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(get_path, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
