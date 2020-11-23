def maxProfit(prices):
    low = float("inf")
    profit = 0
    for i in prices:
        if i < low:
            low = i
        else:
            profit = max(profit,i-low)
    return profit