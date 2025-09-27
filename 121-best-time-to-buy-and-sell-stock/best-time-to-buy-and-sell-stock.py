class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        buy, sell = n - 2, n - 1
        maxSell, maxProfit = prices[sell], 0
        while buy > -1:
            maxSell = max(maxSell, prices[sell])
            maxProfit = max(maxProfit, maxSell - prices[buy])
            sell -= 1
            buy -= 1
        return maxProfit


        