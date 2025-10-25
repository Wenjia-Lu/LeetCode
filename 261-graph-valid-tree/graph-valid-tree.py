class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: fully connected, no cycles

        # adj list
        adjs = [[] for _ in range(n)]
        for a, b in edges:
            adjs[a].append(b)
            adjs[b].append(a)
        
        q = collections.deque([(0, -1)])
        seen = {0}
        while q:
            curr, parent = q.popleft() # current node
            for neighbor in adjs[curr]: # for each adj node
                if neighbor == parent:
                    continue
                if neighbor in seen: # check if it's a cycle
                    return False
                seen.add(neighbor)
                q.append((neighbor, curr))
        return len(seen) == n
        

        