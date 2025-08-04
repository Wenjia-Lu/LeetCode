class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0
        d = [0 for i in range(26)] 
        for c in s1:
            d[ord(c) - ord('a')] += 1

        window = [0 for i in range(26)]
        for r, c in enumerate(s2):
            window[ord(c) - ord('a')] += 1
            if r - l + 1 > len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if d==window:
                return True
        return False
            



