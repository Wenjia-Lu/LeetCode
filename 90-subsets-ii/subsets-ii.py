class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(i, curr):
            print(nums, i ,curr)
            if i == len(nums):
                result.append(curr)
                return

            # take current
            n = nums[i]
            dfs(i+1, curr + [n])
            # not take current
            while i < len(nums) and nums[i] == n:
                i += 1
            dfs(i, curr)

        dfs(0,[])
        return result
        