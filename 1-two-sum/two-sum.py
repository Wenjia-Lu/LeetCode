class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in d:
                return [i, d[comp]]
            d[n] = i
        return []