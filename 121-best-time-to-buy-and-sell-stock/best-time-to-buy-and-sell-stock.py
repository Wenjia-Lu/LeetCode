class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxSell = [0] * n
        highest = 0
        for i in range(n-2, -1, -1):
            highest = max(highest, prices[i+1])
            maxSell[i] = highest

        highest = -1
        for i, price in enumerate(prices):
            highest = max(highest, maxSell[i] - price)
        return max(highest, 0)


        