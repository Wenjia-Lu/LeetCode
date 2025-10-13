class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def dfs(sum, i):
            if sum > target or i > len(candidates) - 1:
                return
            if sum == target:
                result.append(curr.copy())
                return

            n = candidates[i]
            curr.append(n)
            dfs(sum + n, i)
            curr.pop()
            dfs(sum, i + 1)
        
        dfs( 0, 0)
        return result

        