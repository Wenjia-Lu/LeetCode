class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(0) = [1 2 3 4] -> 1 * 0, 2 * 1
        # F(1) = [4 1 2 3] -> 1 * 1, 2 * 2,
        # F(2) = [3 4 1 2] -> 1 * 2, 2 * 3
        # F(3) = [2 3 4 1] -> 1 * 3, 2 * 0

        # F(0) = 0X + 1Y + 2Z
        # F(1) = 1X + 2Y + 0Z <- + X + Y clear Z
        # F(2) = 2X + 0Y + 1Z <- + X clear Y + Z

        # init = 1X + 1Y + 1Z
        sum_ = sum(nums)
        n = len(nums)
        clear = n - 1

        #calc F_0
        curr = 0
        for i, num in enumerate(nums):
            curr += (i * num)

        highest = curr
        for i in range(len(nums)-1):
            curr += sum_
            curr -= (nums[clear] * n)
            clear -= 1
            highest = max(highest, curr)
        return highest
        