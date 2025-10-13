class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []

        def dfs(i, curr):
            if i == len(nums):
                powerset.append(curr.copy())
                return
            
            # take
            dfs(i + 1, curr + [nums[i]])
            # not take
            dfs(i + 1, curr)

        dfs(0, [])
        return powerset

# take, or not to take the 
#       [] <- initialize
#  [1]      [] <- first element, 1: i = 0
# [1,2] [1] [2] [] <- 2: i = 1
# [1,2,3] [1,2] ...
# 2^n possible subsets, time = O(2^n)
# 2^n * O(n) size of a single subset-> n * 2^n
# 2^n stacks -> 2^n + n * 2^n = O(n * 2^n )
