class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        pacifics = set()
        atlantics = set()
        m, n = len(heights), len(heights[0])

        def bfs(q, water_set):
            while q:
                a, b = q.popleft() # starting position
                water_set.add((a,b))
                og_h = heights[a][b] 
                for moveA, moveB in dirs:
                    r, c = a + moveA, b + moveB # next position
                    # bound checking + add to seen
                    if (r,c) not in water_set and 0 <= r < m and 0 <= c < n: 
                        h = heights[r][c]
                        if h >= og_h: # flown from
                            q.append((r,c)) # explore next
                            water_set.add((r,c))
        
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        pacific_starts = [(0, c) for c in range(n)] + [(r,0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        for pair in pacific_starts:
            pacific_queue.append(pair)

        for pair in atlantic_starts:
            atlantic_queue.append(pair)

        bfs(pacific_queue, pacifics)
        bfs(atlantic_queue, atlantics)

        return list(pacifics.intersection(atlantics))




        