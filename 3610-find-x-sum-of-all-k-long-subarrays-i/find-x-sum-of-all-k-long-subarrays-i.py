class Solution:
    def kSum(self, nums, x):
        counts = Counter(nums)
        heap = []
        for n in counts:
            freq = counts[n]
            heapq.heappush(heap, (freq, n))
            if len(heap) > x:
                heapq.heappop(heap)
    
        
        return sum(h[1] * h[0] for h in heap)
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(self.kSum(nums[i:k + i], x))
        
        return res
        