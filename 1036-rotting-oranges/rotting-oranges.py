class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        result = 0
        m,n= len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: # is rotten
                    q.append((i,j))
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
            resolveThisMin = len(q)
            for _ in range(resolveThisMin):
                a, b = q.popleft()
                for moveR, moveC in dirs: # THE ROTTING
                    r,c = a + moveR, b+moveC # explore
                    if 0 <= r < m and 0 <= c < n: # within bounds
                        if grid[r][c] == 1: # is fresh
                            grid[r][c] = 2 # go rot
                            q.append((r,c)) # this infects the next round
            result += 1 


        
        for row in grid:
            if 1 in row:
                return -1
        return max(0, result - 1)

        