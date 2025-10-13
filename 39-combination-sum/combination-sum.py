class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(curr, sum, i):
            if sum > target:
                return
            if sum == target:
                result.append(curr.copy())
                return
            if i == len(candidates):
                return
            
            n = candidates[i]
            # take
            dfs(curr + [n], sum + n, i)
            # not take
            dfs(curr, sum, i + 1)
            
        dfs([], 0, 0)
        return result
       