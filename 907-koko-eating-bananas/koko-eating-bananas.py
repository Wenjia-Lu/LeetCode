class Solution:
    def eating_hours(self, piles, speed):
        hrs = 0
        for pile in piles:
           hrs += math.ceil(pile / speed)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mid = 0
        prev = -10
        while l < r:
            mid = l + (r-l)//2
            time_spent = self.eating_hours(piles, mid)
            print(time_spent, )
            if time_spent > h: # ate too slow
                l = mid + 1
            else:
                r = mid
        return int(l)
        
        