from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    class MaxWithCount:

        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):

        self._elements = []

        self._maximums = []

    def empty(self):

        return len(self._elements) == 0

    def max(self):

        if self.empty():
            return IndexError('pop(): Stack is empty!')

        return self._maximums[-1].max

    def pop(self):

        if self.empty():
            return IndexError('pop(): Stack is empty!')

        n = self._elements.pop()
        current_max = self._maximums[-1].max

        if n == current_max:

            self._maximums[-1].count -= 1

            if self._maximums[-1].count == 0:
                self._maximums.pop()

        return n

    def push(self, n):

        self._elements.append(n)

        if len(self._maximums) == 0:
            self._maximums.append(self.MaxWithCount(n, 1))

        else:

            current_max = self._maximums[-1].max

            if n == current_max:
                self._maximums[-1].count += 1

            elif n > current_max:
                self._maximums.append(self.MaxWithCount(n, 1))

# s = Stack()

# assert(s.empty())

# s.push(1)

# assert(not s.empty())
# assert(s.max() == 1)

# s.pop()

# assert(s.empty())

# s.push(4)
# s.push(6)
# s.push(2)

# assert(s.max() == 6)

# s.pop()

# assert(s.max() == 6)

# s.pop()

# assert(s.max() == 4)

# s.pop()

# assert(s.empty())

# exit()

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
