class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(curr, sum, i):
            if sum > target or i > len(candidates) - 1:
                return
            if sum == target:
                result.append(curr.copy())
                return

            n = candidates[i]
            curr.append(n)
            dfs(curr.copy(), sum + n, i)
            curr.pop()
            dfs(curr.copy(), sum, i + 1)
        
        dfs([], 0, 0)
        return result

        