class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        sell = prices[-1]
        max_profit = 0
        for buy_day in range(n-2, -1,-1):
            cost = prices[buy_day]
            max_profit = max(max_profit, sell - cost) 
            sell = max(sell, cost)
        return max_profit




        