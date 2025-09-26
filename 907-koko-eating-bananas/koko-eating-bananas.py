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
            # print(f"For a speed of {mid}, ate for {time_spent} hours")
            # print(f"l,r ={(l,r)}")
            # print(prev, mid)
            if prev == mid: 
                # print("converged!")
                return int(mid)
            prev = mid

            if time_spent > h: # ate too slow
                l = mid + 1
            elif time_spent == h:
                r = mid
            else:
                r = mid
        return int(l)
        
        