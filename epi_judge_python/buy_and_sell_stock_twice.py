from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice_naive(P: List[float]) -> float:

    def buy_and_sell_stock(P):

        buy_index, max_profit = 0, 0

        for i in range(0, len(P)):

            delta = P[i] - P[buy_index]

            if delta > max_profit:
                max_profit = delta

            if P[i] < P[buy_index]:
                buy_index = i

        return max_profit

    max_global_profit = buy_and_sell_stock(P)

    for i in range(1, len(P) - 1):

        max_global_profit = max(
            max_global_profit,
            buy_and_sell_stock(P[:i]) + buy_and_sell_stock(P[i:])
        )

    return max_global_profit


def buy_and_sell_stock_twice(P):

    max_total_profit = 0.0

    min_buy_price_so_far = float('inf')

    first_buy_and_sell_by = [0] * len(P)

    # Forward pass

    for i, price in enumerate(P):

        min_buy_price_so_far = min(min_buy_price_so_far, price)

        max_total_profit = max(max_total_profit, price - min_buy_price_so_far)

        first_buy_and_sell_by[i] = max_total_profit

    # Backward pass

    max_price_so_far = float('-inf')

    for i, price in reversed(list(enumerate(P[1:], 1))):

        max_price_so_far = max(max_price_so_far, price)

        max_total_profit = max(max_total_profit,
            first_buy_and_sell_by[i-1] + max_price_so_far - price)

    return max_total_profit


# print(buy_and_sell_stock_twice([310,315,275,295]))
# print(buy_and_sell_stock_twice([310,315,275,295,260]))
# print(buy_and_sell_stock_twice([310,315,275,295,260,270,290,230,255,250]))

# exit()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
