class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # know what numbers we have
        best = 0
        for n in nums:
            if n - 1 not in nums:
                seq = n + 1
                while seq in nums:
                    seq += 1
                best = max(best, seq - n)
        return best