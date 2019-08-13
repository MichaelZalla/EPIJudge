from typing import List

from test_framework import generic_test


def is_valid_ip_address_component(c: str) -> bool:

    d = int(c)

    if len(c) > len(str(d)):
        return False

    if d > 255:
        return False

    return True

def get_valid_ip_address(s: str) -> List[str]:

    result = []

    for i in range(0, len(s) - 3):

        a = s[0:i+1]

        if not is_valid_ip_address_component(a):
            continue

        for j in range(i + 1, len(s) - 2):

            b = s[i+1:j+1]

            if not is_valid_ip_address_component(b):
                continue

            for k in range(j + 1, len(s) - 1):

                c = s[j+1:k+1]
                d = s[k+1:len(s)]

                if not is_valid_ip_address_component(c) or not is_valid_ip_address_component(d):
                    continue

                result.append('{}.{}.{}.{}'.format(a, b, c, d))

    return result


# print(get_valid_ip_address('19216811'))

# exit()


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
