class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(nums, subset):
            if not nums:
                result.append(subset[:])
                return

            n = nums.pop()
            backtrack(nums, subset)         # exclude n
            backtrack(nums, subset + [n])   # include n
            nums.append(n)                  # backtrack (undo)

        backtrack(nums, [])
        return result