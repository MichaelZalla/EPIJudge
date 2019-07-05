from test_framework import generic_test


def look_and_say(n: int) -> str:

    def get_run(S, index):

        digit, count = S[index], 1

        while index < len(S) - 1 and S[index + 1] == digit:
            count += 1
            index += 1

        return (digit, count)

    def get_next_look_and_say(L):

        next_sequence = []

        index = 0

        while index < len(L):

            digit, count = get_run(L, index)

            next_sequence += [str(count)] + [digit]

            index += count

        return (''.join(next_sequence))

    i, L = 1, '1'

    while i < n:

        L = get_next_look_and_say(L)

        i += 1

    return L


# print(look_and_say(1))
# print(look_and_say(2))
# print(look_and_say(3))
# print(look_and_say(4))
# print(look_and_say(5))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
