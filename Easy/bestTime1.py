# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """List[int] -> int
        Finds max profit from buying one stock and selling it"""
    max_profit = 0
    profits = []
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profits.append(prices[i] - prices[j])
    print(profits)
    max_profit = abs(min(min(profits), max_profit))
    return max_profit


# Tests
s = maxProfit([7,1,5,3,6,4]) # 5
print(s)

s = maxProfit([7,6,4,3,1]) # 0
print(s)
