class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        for i in range(len(strs[0])): # O(n)
            pre = set()
            for s in strs:
                if i > len(s) - 1:
                    return s
                pre.add(s[i])
                if len(pre) > 1:
                    return s[:i]
        return strs[0]