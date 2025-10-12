class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, subset):
            if nums == []:
                result.append(copy.deepcopy(subset))
                return
            
            n = nums[-1]
            backtrack(nums[:-1], subset)
            backtrack(nums[:-1], subset + [n])

        backtrack(nums, [])
 
        return result