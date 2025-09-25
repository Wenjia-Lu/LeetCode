class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # total cost at n = cost of n + min(total cost at n_1, total cost at n-2)
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1] # min(cost0 + cost1, cost1) is just cost1
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])