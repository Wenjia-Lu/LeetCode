class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def dfs(sum, i):
            if sum > target:
                return
            if sum == target:
                result.append(curr.copy())
                return
            if i == len(candidates):
                return
            
            # take
            n = candidates[i]
            curr.append(candidates[i])
            dfs(sum + n, i)
            # not take
            curr.pop()
            dfs(sum, i + 1)
            
        dfs( 0, 0)
        return result
       