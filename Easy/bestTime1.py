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

def maxProfit(prices):
    i = 0
    j = 1
    max_profit = 0
    while j in range(len(prices)):
        max_profit = max(prices[j] - prices[i], max_profit)
        
        # i has the potential to keep growing
        if prices[j] - prices[i] > 0:
            # keep i
            pass
        else:
            # we want to move i
            i = j
        j += 1
        
    return max_profit

# Tests
s = maxProfit([7,1,5,3,6,4]) # 5
print(s)

s = maxProfit([7,6,4,3,1]) # 0
print(s)
