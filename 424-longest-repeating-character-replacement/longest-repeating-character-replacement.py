class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans, l, maxf = 0, 0, 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            maxf = max(maxf, d[s[r]])

            while (r - l + 1) - maxf > k: # more replaces than chances
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans