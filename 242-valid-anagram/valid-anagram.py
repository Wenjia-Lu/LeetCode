class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        l = [0 for i in range(26)]
        for i in range(len(s)):
            l[ord(s[i]) - 97] += 1
            l[ord(t[i]) - 97] -= 1
        
        return l == [0 for i in range(26)]
        