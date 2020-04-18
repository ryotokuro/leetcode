# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    """List[int] -> int
    Finds max profit from buying one stock and selling it"""
    buy = 0
    sell = 1
    max_profit = 0
    while sell in range(len(prices)):
        profit = prices[sell] - prices[buy]
        max_profit = max(profit, max_profit)
        
        # the buy stock still has potential to grow
        if profit < 0:
            # change to a buy stock with higher potential
            buy = sell
        # move sell stock (j) through the list (days)
        sell += 1
        
    return max_profit


# Tests
s = maxProfit([7,1,5,3,6,4]) # 5
print(s)

s = maxProfit([7,6,4,3,1]) # 0
print(s)
