# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """List[int] -> int
        Finds max profit from buying one stock and selling it"""
    profits = []
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profits.append(prices[j] - prices[i])

    print(profits)
    max_profit = max(max(profits), 0)
    return max_profit


# Tests
s = maxProfit([7,1,5,3,6,4]) # 5
print(s)

s = maxProfit([7,6,4,3,1]) # 0
print(s)
