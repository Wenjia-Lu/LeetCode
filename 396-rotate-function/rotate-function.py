class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(0) = 0X + 1Y + 2Z
        # F(1) = 1X + 2Y + 0Z <- + X + Y clear Z
        # F(2) = 2X + 0Y + 1Z <- + X clear Y + Z

        # init = 1X + 1Y + 1Z
        sum_ = sum(nums)
        n = len(nums)

        #calc F_0
        curr = 0
        for i, num in enumerate(nums):
            curr += (i * num)

        highest = curr
        for clear in range(n-1, 0, -1):
            curr += sum_ - (nums[clear] * n)
            highest = max(highest, curr)
        return highest
        