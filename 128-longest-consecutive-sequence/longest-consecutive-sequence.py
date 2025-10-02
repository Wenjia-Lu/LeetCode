class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nset = set(nums)
        best = 1
        for n in nset:
            if n - 1 not in nset:
                next = n + 1
                curr = 1
                while next in nset:
                    curr += 1
                    best = max(best, curr)
                    next += 1
        return best

