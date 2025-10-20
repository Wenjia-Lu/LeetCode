class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        seen = set()
        m, n = len(board), len(board[0])
        def bfs(r,c):
            region = set()
            q = deque()
            q.append((r,c))
            region.add((r,c))
            seen.add((r,c))
            escaped = False

            while q:
                a, b = q.popleft() # current tile
                for moveA, moveB in dirs:
                    r, c = a + moveA, b + moveB # next tile
                    if 0 <= r < m and 0 <= c < n: # in bounds
                        if (r,c) not in seen: # explore next
                            seen.add((r,c))
                            if board[r][c]=="O":
                                q.append((r,c)) 
                                region.add((r,c))
                    else: # escaped
                        escaped = True
            
            return region if not escaped else set()
        
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r,c) not in seen:
                    captured = bfs(r,c)
                    for a,b in captured:
                        board[a][b] = "X"