class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        a, b = 0, len(x) - 1
        while a < b:
            if x[a] != x[b]:
                return False
            a += 1
            b -= 1
        return True
        