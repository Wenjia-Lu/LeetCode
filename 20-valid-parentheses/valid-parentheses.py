class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '(': 1,
            ')': 11,
            '{': 2,
            '}': 12,
            '[': 3,
            ']': 13,
        }
        stack = []
        for c in s:
            if d[c] < 5:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                # if head is the matching right brace
                if d[stack[-1]] == d[c] - 10:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
