from test_framework import generic_test


def evaluate(S: str) -> int:

    stack, end = [], len(S)

    for start in reversed(range(len(S))):

        if S[start] == ',':

            stack.append(S[start+1:end])

            end = start

    stack.append(S[0:end])

    results = []

    while len(stack):

        token = stack.pop()

        if token in '+-*/':

            operation = token

            operand1 = results.pop()

            operand2 = results.pop()

            if operation is '+':
                result = operand2 + operand1
            elif operation is '-':
                result = operand2 - operand1
            elif operation is '*':
                result = int(operand2 * operand1)
            else: # if operation is '/':
                result = int(operand2 / operand1)

            results.append(result)

        else:

            results.append(int(token))


    return results[-1]


def evaluate_alternate(S: str) -> int:

    OPERATORS = {
        '+': lambda op2, op1: op1 + op2,
        '-': lambda op2, op1: op1 - op2,
        '*': lambda op2, op1: op1 * op2,
        '/': lambda op2, op1: int(op1 / op2),
    }

    results = []

    for token in S.split(','):

        if token in OPERATORS:

            results.append(
                OPERATORS[token](
                    results.pop(),
                    results.pop()
                )
            )

        else:

            results.append(int(token))

    return results[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate_alternate))
