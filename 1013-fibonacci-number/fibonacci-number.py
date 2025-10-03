class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        memo = [0] * (n+1)
        memo[1] = 1
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
