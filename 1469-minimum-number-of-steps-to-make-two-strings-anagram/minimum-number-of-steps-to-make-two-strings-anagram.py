class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = [0 for i in range(26)]
        for i in range(len(s)):
            d[ord(s[i]) - ord('a')] += 1
            d[ord(t[i]) - ord('a')] -= 1
        sa = 0
        ta = 0
        for i in d:
            if i > 0:
                sa += abs(i)
            elif i < 0:
                ta += abs(i)
        return min(sa, ta) + abs(len(s) - len(t))

    
# bab -> a:1, b:2 -> a: 0, b: 1
# aba -> a:2, b:1 -> a: 1, b: 0 = 1 change
# [a, b] -> [-1, 1] -> sa: 1, ta: 1 -> 1

# abc -> b: 1, c: 1
# abd -> c: 1 = 1 change
# [a, b, c, d] -> [0, 0, 1, -1] -> 1 change

# acdd -> d: 2 = 2 changes
# accc -> c: 3
# [a, b, c, d] -> [0, 0, -2, 2]

# leeod
# praic