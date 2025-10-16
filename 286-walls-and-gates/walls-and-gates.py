class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ninf = 2**31 - 1
        q = collections.deque()

        m,n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            a,b = q.popleft() # current room
            for moveR, moveC in dirs:
                r, c = a+moveR, b+moveC # explore
                if 0 <= r < m and 0 <= c < n: # if within bounds
                    if rooms[r][c] == ninf: # is empty
                        rooms[r][c] = 1 + rooms[a][b] # calc distance
                        q.append((r,c))
    
        