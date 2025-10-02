class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nset = set(nums)
        for n in nset:
            if n - 1 not in nset:
                next = n + 1
                while next in nset:
                    next += 1
                best = max(best, next - n)
        return best

