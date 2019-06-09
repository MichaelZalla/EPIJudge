from typing import List

from test_framework import generic_test


def num_permutations_for_final_score(final_score: int,
                                     plays: List[int]) -> int:

    def num_permutations_memoized(score, cache = {0:1}):

        if score in cache:
            return cache[score]

        sum = 0

        for play in plays:
            if (score-play) > -1:
                sum += num_permutations_memoized(score - play, cache)

        cache[score] = sum

        return cache[score]

    return num_permutations_memoized(final_score)

def num_combinations_for_final_score(final_score, plays):

    # For each play, there is exactly 1 combination of less-than-or-equal-to
    # plays that sum to zero (i.e., no plays)

    num_combinations_for_score = [[1] + [0] * final_score for play in plays]

    # For each individual play...

    for play_index in range(len(plays)):

        play_value = plays[play_index]

        # For each non-zero score from 1 to final_score...

        for score_index in range(1, final_score + 1):

            # For the given score, we can elect not to 'choose' this play as the
            # final play, in which case we'll reach our score only by using
            # lesser-value plays

            without_this_play = num_combinations_for_score[play_index - 1][score_index] \
                if play_index > 0 else 0

            # Alternately, we can 'choose' this play as the final play to reach
            # our score; there are exactly num_combinations_for_score[play_index][score_index - play_value]
            # ways in which we could reach our score by adding one of these plays

            with_this_play = num_combinations_for_score[play_index][score_index - play_value] \
                if play_value <= score_index else 0

            # We combine our 'with' and 'without' options to reach a final count
            # for this score (and set of plays)

            num_combinations_for_score[play_index][score_index] = without_this_play + with_this_play

    return num_combinations_for_score[-1][-1]


# plays = [1,2,3,6]

# print(num_combinations_for_final_score(0, plays))
# print(num_combinations_for_final_score(1, plays))
# print(num_combinations_for_final_score(2, plays))
# print(num_combinations_for_final_score(3, plays))
# print(num_combinations_for_final_score(4, plays))
# print(num_combinations_for_final_score(5, plays))
# print(num_combinations_for_final_score(6, plays))

# plays = [2,3,7]

# print(num_combinations_for_final_score(12, plays))

# exit()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
