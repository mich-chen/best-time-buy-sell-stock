from typing import List

def maxProfit(prices: List[int]) -> int:

    if not prices:
        return 0

    maxprofit = 0
    minprice = max(prices)

    for price in prices:
        if price < minprice:
            minprice = price
        maxprofit = max(maxprofit, price - minprice)

    return maxprofit


if __name__ == '__main__':

    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
