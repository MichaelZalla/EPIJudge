from typing import Set

from test_framework import generic_test

import collections
import string


def transform_string_naive(D, s, t):

    def distance(A, B):

        # Finds edit distance (via replacements) for strings of equal length;

        differences = 0

        for i in range(len(A)):
            if A[i] != B[i]:
                differences += 1

        return differences

    def get_path_length(V, E, start, end):

        # Generic single-source shortest path implementation using BFS

        frontier, pred = collections.deque([start]), { start: None }

        while frontier:

            node = frontier.popleft()

            if node == end:

                path, prev = [end], pred[end]

                while prev is not None:
                    path.append(prev)
                    prev = pred[prev]

                return len(path) - 1

            neighbors = E[node]

            for n in [n for n in neighbors if n not in pred]:
                pred[n] = node
                frontier.append(n)

        return -1

    if s == t:
        return 0

    if len(s) != len(t) or s not in D or t not in D:
        return -1

    # Model all words in D (of same length as 's') using a graph; an undirected
    # edge between nodes (u,v) indicates that a single character replacement can
    # be used to transform u to v, and vice-versa;

    V = [word for word in D if len(word) == len(s)]

    E = [[] for _ in range(len(V))]

    # Note that the time complexity of generating the graph is O(m*n^2), where m
    # is the length of s and t; if we can assume that n > m, then this can be
    # simplified to O(n^2);

    for i in range(len(V)):
        for j in range(len(V)):
            if j != i and distance(V[i], V[j]) == 1:
                E[i].append(j)

    # Finds a shortest path length from s to v in G = (V, E) using BFS;

    return get_path_length(V, E, V.index(s), V.index(t))


def transform_string(D: Set[str], s: str, t: str) -> int:

    # We'll use a queue to hold 'unvisited' words that we've come across in D;

    Q, distance = collections.deque([s]), { s: 0 }

    while Q:

        word = Q.popleft()

        # To improve runtime performance when the size of our dictionary n grows
        # to be much larger than m (the length of s and t), we can generate a
        # set of potential neighboring words in D and check for their presence
        # in D in constant time; generating candidates is bounded by O(m);

        for i in range(len(word)):

            for char in string.ascii_lowercase:

                if char != word[i]:

                    perm = word[:i] + char + word[i+1:]

                    if perm in D and perm not in distance:

                        # If we've traversed to t, return a final distance;

                        if perm == t:
                            return distance[word] + 1

                        # Otherwise, record a shortest 'path' from s to perm,
                        # and schedule perm for visiting later;

                        distance[perm] = distance[word] + 1

                        Q.append(perm)

    # No path to t was found from s

    return -1


# print(transform_string(['bat','cot','dog','dag','dot','cat'], 'cat', 'dog'))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
