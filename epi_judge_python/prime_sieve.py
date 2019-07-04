from typing import List

from test_framework import generic_test


def generate_primes_trial_division(n: int) -> List[int]:

    primes = []

    for i in range(2, n):

        is_prime = True

        for p in primes:
            if i % p == 0:
                is_prime = False

        if is_prime:
            primes.append(i)

    return primes

def generate_primes_seive(n):

    primes, is_prime = [], [False, False] + [True] * (n - 1)

    for p in range(2, n):

        if is_prime[p]:

            primes.append(p)

            for m in range(p+p, n + 1, p):
                is_prime[m] = False

    return primes


def generate_primes_seive_optimized(n: int) -> List[int]:

    if n < 2:
        return []

    primes = [2]

    # We maintain an index-to-value mapping such that v = 2i + 3; for i, this
    # solves to i = (p - 3) // 2; note that this mapping excludes values 0, 1,
    # and 2 from its range; 0 and 1 are not prime, by definition; 2 is trivally
    # know to be a prime;

    last_valid_candidate_index = (n - 3) // 2

    # Our array of candidates must be large enough for the final candidate (n);

    num_candidates = last_valid_candidate_index + 1

    is_prime = [True] * num_candidates

    # is_prime includes a position for all potential candidates from 3..n

    for index in range(num_candidates):

        # If this candidate has not already been invalidated as a non-prime

        if is_prime[index]:

            # Map index to its value

            p = 2*index + 3

            primes.append(p)

            # idx(p^2) = (p^2 - 3) // 2
            # idx(p^2) = ((2*i + 3)^2 - 3) // 2
            # idx(p^2) = ((4*i^2 + 12*i + 9) - 3) // 2
            # idx(p^2) = (4*i^2 + 12*i + 6) // 2
            # idx(p^2) = 2*i^2 + 6*i + 3

            index_of_p_squared = 2 * index**2 + 6 * index + 3

            for multiple_of_p in range( \
                index_of_p_squared, last_valid_candidate_index + 1, p):

                is_prime[multiple_of_p] = False

    return primes


# print(generate_primes_trial_division(18))
# print(generate_primes_seive(18))
# print(generate_primes_seive_optimized(18))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes_seive_optimized))
