from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:

    def __init__(self, capacity: int) -> None:

        self._size = self.start = self.next = 0

        self.L = [None] * capacity


    def enqueue(self, elem: int) -> None:

        # Checks whether there is a vacancy before start in the existing list

        if self.size() < len(self.L):

            # Fills in the vacant end position and advances next pointer

            self.L[self.next] = elem

            self.next = (self.next + 1) % len(self.L)

        else:

            # Otherwise, the current list is full

            if self.start == 0:

                # If the list begins at the first index position, simply append
                # a new item at the end

                self.L = self.L + [elem]

            else:

                # Otherwise, we need to shift L[start:] right by one, making a
                # new position vacant at L[next]

                self.L = self.L + [None]

                for i in reversed(range(self.start, len(self.L) -1)):
                    self.L[i+1] = self.L[i]

                self.L[self.next] = elem

                self.start, self.next = self.start + 1, self.next + 1

        # Increments size

        self._size += 1


    def dequeue(self) -> int:

        if not self.size():
            return IndexError('dequeue: Called on an empty queue!')

        value = self.L[self.start]

        # Advances the start pointer by one position, and incremeents size

        self.start = (self.start + 1) % len(self.L)

        self._size -= 1

        return value

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
