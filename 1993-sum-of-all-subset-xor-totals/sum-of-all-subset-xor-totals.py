class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = [0]

        def dfs(i, xor=None):
            if i == len(nums):
                result[0] += (xor if xor else 0)
                return
            
            if not xor:
                dfs(i + 1, nums[i])
            else:
                dfs(i+1, xor ^ nums[i])
            dfs(i + 1, xor)

        dfs(0)
        return result[0]
            

        