class Solution:
    def eating_hours(self, piles, speed):
        hrs = 0
        for pile in piles:
           hrs += math.ceil(pile / speed)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, sum(piles)
        mid = 0
        # print(l,r)
        prev = -10
        while l < r:
            mid = l + (r-l)//2
            time_spent = self.eating_hours(piles, mid)
            # if prev == mid:
            #     return int(mid)
            # prev = mid

            if time_spent > h: # ate too slow
                l = mid + 1
            else:
                r = mid
        return int(l)
        
        