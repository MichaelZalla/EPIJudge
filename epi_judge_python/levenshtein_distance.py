from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:

    # Initializes results for empty-string-to-B (i.e., all insertions) and
    # A-to-empty-string (i.e., all deletions); a placeholder is used to mark the
    # remaining prefix-to-prefix problems;

    prefix_distances = [ \
        list(range(len(B) + 1)) if i == 0 else [i] + [float('inf')] * len(B) \
        for i in range(len(A) + 1)]

    # We can iteratively compute our distances table in either row-first or
    # column-first priority; the order doesn't matter;

    for j in range(1, len(B) + 1):

        for i in range(1, len(A) + 1):

            # The added cost of the given transformation (subproblem) depends on
            # the final letters in both prefixes;

            last_in_A_prefix, last_in_B_prefix = A[i-1], B[j-1]

            if last_in_A_prefix == last_in_B_prefix:

                # If the letters match, we can transform one prefix into the
                # other using prefix_distances[i-1][j-1] edit actions;

                prefix_distances[i][j] = prefix_distances[i-1][j-1]

            else:

                # Otherwise, consider each way we might possible arrive at this
                # subproblem, and choose the lowest-cost strategy, adding the
                # cost of the final edit;

                last_as_substitution = prefix_distances[i-1][j-1]
                last_as_insertion = prefix_distances[i][j-1]
                last_as_deletion = prefix_distances[i-1][j]

                prefix_distances[i][j] = 1 + min(
                    last_as_substitution,
                    last_as_insertion,
                    last_as_deletion
                )

    # The global minimum edit distance will be populated in the bottom-right of
    # our distances table;

    return prefix_distances[-1][-1]


# print('Distance between "A" and "A" is ', levenshtein_distance('A', 'A'))
# print('Distance between "A" and "AA"  is ', levenshtein_distance('A', 'AA'))
# print('Distance between "A" and "AAA"  is ', levenshtein_distance('A', 'AAA'))
# print('Distance between "AA" and "A"  is ', levenshtein_distance('AA', 'A'))
# print('Distance between "AA" and "AA" is ', levenshtein_distance('AA', 'AA'))
# print('Distance between "AA" and "AAA"  is ', levenshtein_distance('AA', 'AAA'))
# print('Distance between "AAA" and "A"  is ', levenshtein_distance('AAA', 'A'))
# print('Distance between "AAA" and "AA"  is ', levenshtein_distance('AAA', 'AA'))
# print('Distance between "A" and "B" is ', levenshtein_distance('A', 'B'))
# print('Distance between "A" and "AB" is ', levenshtein_distance('A', 'AB'))
# print('Distance between "A" and "BA" is ', levenshtein_distance('A', 'BA'))
# print('Distance between "C" and "AB" is ', levenshtein_distance('C', 'AB'))
# print('Distance between "C" and "ABC" is ', levenshtein_distance('C', 'ABC'))
# print('Distance between "ABC" and "CAT" is ', levenshtein_distance('ABC', 'CAT'))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
