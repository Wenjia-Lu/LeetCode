class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nset = set(nums)
        best = 1
        for n in nset:
            if n - 1 not in nset:
                curr = 1
                while n + 1 in nset:
                    curr += 1
                    best = max(best, curr)
                    n += 1
        return best

