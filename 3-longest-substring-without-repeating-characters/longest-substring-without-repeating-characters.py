class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        longest = 0
        for r, c in enumerate(s):
            # only need to shift l to ignore duplicates if 
            #   the dup is WITHIN the current window
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            longest = max(longest, r - l + 1)
            seen[c] = r
        return longest

# abba
# 