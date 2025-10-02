class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nset = set(nums)
        for n in nset:
            if n - 1 not in nset:
                curr = 1
                while n + 1 in nset:
                    curr += 1
                    n += 1
                best = max(best, curr)
        return best

