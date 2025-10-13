class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, curr):
            if nums == []:
                result.append(curr)
                return

            for i in range(len(nums)):
                n = nums[i]
                copy = nums.copy()
                copy.pop(i)
                dfs(copy, curr + [n])

        dfs(nums, [])
        return result

# dfs([1,2,3], []) -> dfs([1,2,3],[2])
# dfs([2,3], [1]) -> dfs([2], [1,3]) -> [1,3,2]
# dfs([3], [1, 2]) -> returned
# dfs([], [1, 2, 3]) -> returned result = [[1,2,3]]
