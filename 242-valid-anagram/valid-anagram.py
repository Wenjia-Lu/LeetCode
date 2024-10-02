class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hs = [0 for i in range(26)]
        for i in range(len(s)):
            hs[ord(s[i]) - ord('a')] += 1
            hs[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(hs)):
            if hs[i] != 0:
                return False
        
        return True
            