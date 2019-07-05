from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueNaive:

    def __init__(self):
        self.queue = []
        self.temp = []

    def enqueue(self, elem: int) -> None:

        while self.queue:
            self.temp.append(self.queue.pop())

        self.queue.append(elem)

        while self.temp:
            self.queue.append(self.temp.pop())

    def dequeue(self) -> int:

        if not self.queue:
            raise IndexError('Tries to dequeu from empty queue!')

        return self.queue.pop()


class Queue:

    def __init__(self):
        self.en, self.de = [], []

    def enqueue(self, elem: int) -> None:

        self.en.append(elem)

    def dequeue(self) -> int:

        if not self.de:
            while self.en:
                self.de.append(self.en.pop())

        if not self.de:
            raise IndexError('Tries to dequeu from empty queue!')

        return self.de.pop()


# q = Queue()

# q.enqueue('A')
# q.enqueue('B')
# q.enqueue('C')

# print(q.dequeue())
# print(q.dequeue())

# q.enqueue('D')

# print(q.dequeue())
# print(q.dequeue())

# exit()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
