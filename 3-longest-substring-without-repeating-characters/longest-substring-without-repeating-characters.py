class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set() # fast insert & delete, avging O(1)
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
            
 # r = 3, l = 0 -> 4, window is only 3!
 # abcbd
 # 