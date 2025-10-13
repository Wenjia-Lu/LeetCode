class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        curr = []
        def dfs(i):
            if i == len(nums):
                subsets.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            dfs(i + 1)
        dfs(0)

        result = 0
        for s in subsets:
            ans = 0
            if len(s) > 1:
                ans = s[0] ^ s[1]
                for i in range(2, len(s)):
                    ans = ans ^ s[i]
            else:
                ans = 0 if s == [] else s[0]
            print(s, ans)
            result += ans
        return result
            

        