class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] ** 2 + point[1] ** 2

        points.sort(key=dist)

        return points[:k]

        
        

        