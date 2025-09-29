class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        best = 0
        for r, c in enumerate(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            best = max(best, r - l + 1)
        return best
#
# abba
# 