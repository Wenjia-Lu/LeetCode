class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        n = len(nums)
        for n in nums:
            if n != val:
                nums[p1] = n
                p1 += 1
        return p1