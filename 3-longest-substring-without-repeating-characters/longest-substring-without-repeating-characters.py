class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        longest = 0
        for r, c in enumerate(s):
            if c in window and window[c] >= l:
                l = window[c] + 1
            longest = max(longest, r - l + 1)
            window[c] = r
        return longest

# Optimization: instead of while, keep track of indices