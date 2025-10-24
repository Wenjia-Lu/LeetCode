class Solution:
    def hasSameDigits(self, s: str) -> bool:

        def mod(s):
            
            n = int(s)
            res = ""
            for i in range(len(s)-1):
                res += f"{(int(s[i]) + int(s[i+1])) % 10}"
            return res


        while len(s) > 2:
            s = mod(s)
        
        return s[0] == s[1]