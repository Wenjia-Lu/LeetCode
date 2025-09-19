def expV(a, b, op):
    print(a, b, op)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return int(a / b)

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = []
        for token in tokens:
            if token[-1] in '0123456789':
                nums.append(int(token))
            else:
                ops.append(token)
            if len(ops) > 0 and len(nums) >= 2:
                a = expV(nums[-2], nums[-1], ops[-1])
                nums.pop()
                nums.pop()
                ops.pop()
                nums.append(a)
        return nums[-1]
                
        