class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        size = 1
        res = s[0]

        def dfs(l, r):
            nonlocal size
            nonlocal res

            if l < 0 or r == n:
                return

            if s[l] == s[r]:

                if r - l + 1 > size:
                    size = r - l + 1
                    res = s[l:r+1]

                dfs(l-1, r+1)
        
        for i in range(n-1):
            dfs(i, i)
            dfs(i, i + 1)
        
        return res