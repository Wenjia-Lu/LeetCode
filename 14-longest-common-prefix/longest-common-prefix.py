class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        for i in range(len(strs[0])): # O(n)
            c = strs[0][i]
            for s in strs:
                if i > len(s) - 1:
                    return s
                if c != s[i]:
                    return s[:i]
        return strs[0]