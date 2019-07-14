from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    if len(prices) < 2:
        return 0

    buy_index, max_profit = 0, 0

    for i in range(1, len(prices)):

        delta = prices[i] - prices[buy_index]

        if delta > max_profit:
            max_profit = delta

        if prices[i] < prices[buy_index]:
            buy_index = i

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
