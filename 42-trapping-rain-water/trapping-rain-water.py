class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        a, b = 0, len(height) - 1
        maxL, maxR = height[a], height[b]
        total = 0
        while a < b:
            if maxL < maxR:
                a += 1
                total += max(0, maxL - height[a])
                maxL = max(maxL, height[a])
            else:
                b -= 1
                total += max(0, maxR - height[b])
                maxR = max(maxR, height[b])
        return total