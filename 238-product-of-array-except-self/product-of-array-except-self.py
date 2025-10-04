class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        post = 1
        arr = [1] * n 
        for i in range(n):
            arr[i] *= pre
            pre *= nums[i]
            arr[n - 1 - i] *= post
            post *= nums[n - 1 - i]
        
        return arr


        