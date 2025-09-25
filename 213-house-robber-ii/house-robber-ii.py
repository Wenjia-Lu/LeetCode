class Solution:
    def line_rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0] * n
        print(nums)
        dp[0] = nums[0]
        dp[1] =  max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return max(dp[n-1], dp[n-2])

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        return max(self.line_rob(nums[:-1]), self.line_rob(nums[1:]))
       