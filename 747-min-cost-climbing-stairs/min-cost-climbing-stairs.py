class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * (n+1)
        memo[0] = cost[0]
        memo[1] = cost[1]
        cost.append(0)
        for i in range(2, n + 1):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
        
        return min(memo[n], memo[n-1])