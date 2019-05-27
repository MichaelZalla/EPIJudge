import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A: List[Event]) -> int:

    Signal = collections.namedtuple('Signal', ('time', 'event', 'type'))

    # Transforms our event queue into a list of signals

    signals = []

    for event in A:
        signals.append(Signal(event.start, event, 'start'))
        signals.append(Signal(event.finish, event, 'finish'))

    # Stable sort allows us to prioritize start signals over finish signals

    signals.sort(key = lambda signal: 0 if signal.type is 'start' else 1)
    signals.sort(key = lambda signal: signal.time)

    max_concurrent_events = pending_finish_signals = 0

    for signal in signals:

        # Note that in the case where one event finishes when another begins, we
        # need to make certain that the start signal is processed first; this is
        # because the test cases expect that events may overlap at the limit;

        if signal.type == 'start':
            # print('{0} Started event {1}'.format('\t' * pending_finish_signals, signal.event))
            pending_finish_signals += 1
            # print('{0} Pending signals: {1}'.format('\t' * pending_finish_signals, pending_finish_signals))
            max_concurrent_events = max(max_concurrent_events, pending_finish_signals)
        else:
            pending_finish_signals -= 1
            # print('{0} Finished event {1}'.format('\t' * pending_finish_signals, signal.event))
            # print('{0} Pending signals: {1}'.format('\t' * pending_finish_signals, pending_finish_signals))

    return max_concurrent_events

# Q0 = []
# Q1 = [Event(0, 1)]
# Q2 = [Event(0, 1),Event(1, 2),Event(2, 3)]
# Q3 = [Event(0, 1),Event(0, 2),Event(0, 3)]
# Q4 = [Event(0, 2),Event(1, 3),Event(2, 4)]

# print(find_max_simultaneous_events(Q0))
# print(find_max_simultaneous_events(Q1))
# print(find_max_simultaneous_events(Q2))
# print(find_max_simultaneous_events(Q3))
# print(find_max_simultaneous_events(Q4))

# exit()

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
