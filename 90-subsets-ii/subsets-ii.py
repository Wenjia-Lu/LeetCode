class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []
        # time = 2^n iterations with max n ops per iter = n 2^n
        # not sure if we worry about sort() time complexity
        # space = curr = O(n) axill, stack space = O(n)

        def dfs(i):
            if i == len(nums):
                result.append(curr.copy())
                return

            # take current
            n = nums[i]
            curr.append(n)
            dfs(i+1)
            curr.pop()
            # not take current
            while i < len(nums) and nums[i] == n:
                i += 1
            dfs(i)

        dfs(0)
        return result
        