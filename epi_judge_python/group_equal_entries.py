import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))

def group_by_age_in_place(students: List[Person]) -> None:

    def partition(S, start, end, pivot):

        i, j = start, end

        while i < j:

            if S[i].age == pivot:
                i += 1
            elif S[j].age != pivot:
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i, j = i + 1, j - 1

    i, partitioned = 0, {}

    while i < len(students):

        age = students[i].age

        if not age in partitioned:

            partition(students, i, len(students) - 1, age)

            partitioned[age] = True

        i += 1

    return students

def group_by_age_hash_swap(students: List[Person]) -> None:

    age_to_count = collections.Counter([student.age for student in students])
    age_to_offset, offset = {}, 0

    # Logically partitions the array into m subarrays, with boundaries denoted
    # in an age_to_offset table

    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    while age_to_offset:

        # Parameters of next swap

        from_age = next(iter(age_to_offset))
        from_index = age_to_offset[from_age]
        to_age = students[from_index].age
        to_index = age_to_offset[students[from_index].age]

        # Swap the entries

        students[from_index], students[to_index] = \
            students[to_index], students[from_index]

        # Update our offset table, as we've just placed a 'to_age' element

        age_to_count[to_age] -= 1

        # First 'to_age' element appearing in our table was just swapped out;
        # also possibly the last

        if age_to_count[to_age]:
            age_to_offset[to_age] = to_index + 1
        else:
            del age_to_offset[to_age]

# S0 = []
# S1 = [Person(18, 'Elisa'),Person(17, 'Luke'),Person(17, 'Lewis'),Person(16, 'Steve'),Person(17, 'Laura'),Person(17, 'Larabel'),Person(18, 'Edgar')]

# print(group_by_age(S0))
# print(group_by_age(S1))

# exit()

@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age_hash_swap, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
