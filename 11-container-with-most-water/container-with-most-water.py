class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        v = 0
        while a < b:
            h = min(height[a], height[b])
            v = max(v, h * (b-a))
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return v
        