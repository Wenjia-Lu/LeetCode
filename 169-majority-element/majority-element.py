class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        

        vote = 0
        num = nums[0]
        for n in nums:
            if n == num:
                vote += 1
            else:
                vote -= 1
            if vote <= 0:
                num = n
                vote = 1
        return num