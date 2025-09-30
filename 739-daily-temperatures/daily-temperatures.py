class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < t:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans

# when we look at the current temperature:
# 0. if stack is empty, then we just append current and move on
# 1. look into stack, see how many we can pop off
# 2. add current tmp into the stack


        