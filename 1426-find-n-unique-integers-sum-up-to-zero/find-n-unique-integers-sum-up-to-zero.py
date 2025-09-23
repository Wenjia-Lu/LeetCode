class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 != 0:
            ans.append(0)
            n -= 1
        n /= 2
        while n != 0:
            ans.append(n)
            ans.append(n * -1)
            n -= 1
        return ans

        