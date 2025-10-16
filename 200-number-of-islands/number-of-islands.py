# import queue

# q = queue.Queue()
# q.put('task1') # Add to the rear (enqueue)
# q.put('task2')
# print(q.get()) # Remove from the front (dequeue)
# print(q.get())

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # time = size grid
        # space = size grid
        if not grid:
            return 0
        result = 0

        directions = [[-1, 0],[1,0],[0,-1],[0,1]]
        q = collections.deque()

        def visit(r,c):
            while q:
                a, b = q.popleft() # get current land

                for R, C in directions: # add its neighbors
                    r,c = a+R, b+C
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "0"

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result += 1
                    q.append((r,c))
                    grid[r][c] = "0"
                    visit(r,c)
        return result
        