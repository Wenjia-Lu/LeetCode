class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums: # n is the start of a sequence
                seq = n + 1
                while seq in nums:
                    seq += 1    
                # at this point, seq is 1 more than end of this seq
                best = max(best, seq - n)
        return best


    
