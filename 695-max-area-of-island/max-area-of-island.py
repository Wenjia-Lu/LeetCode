class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        def bfs(r, c): # return the area of the current land
            q = collections.deque()
            q.append((r,c))
            area = 0
            directions = [(-1,0), (1,0), (0,1), (0,-1)]

            while q:
                r, c = q.popleft() # current land
                area += 1
                grid[r][c] = 0

                for moveR, moveC in directions:
                    R, C = r + moveR, c + moveC
                    if 0 <= R < len(grid) and 0 <= C < len(grid[0]) and grid[R][C] == 1:
                        q.append((R,C))
                        grid[R][C] = 0
            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    result = max(result, bfs(r,c))
        return result

# 0 0
# 0 1