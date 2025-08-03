class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                m = nums[l] + nums[r] + n
                if  m > 0:
                    r -= 1
                    # while r > l and nums[r] == nums[r+1]:
                    #     r-=1
                elif m < 0:
                    l += 1
                    # while l < len(nums) and nums[l] == nums[l-1]:
                    #     l+=1
                else:
                    item = [nums[l], nums[r], n]
                    ans.append(item)
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
        return ans

