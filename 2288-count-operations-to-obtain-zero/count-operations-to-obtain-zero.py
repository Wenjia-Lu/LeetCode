class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2: # 14 and 3
            if num1 > num2:
                ops += num1 // num2 # op += 4
                num1 %= num2 # 2
            else:
                ops += num2 // num1 # op += 1
                num2 %= num1 # 1
        return ops
        