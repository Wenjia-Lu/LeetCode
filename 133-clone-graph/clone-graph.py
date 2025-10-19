"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        d = {}

        q = collections.deque()
        q.append(node)
        d[node] = Node(val=node.val)

        seen = set()
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in seen:
                    d[neighbor] = Node(val=neighbor.val)
                    seen.add(neighbor)
                    q.append(neighbor)
                d[n].neighbors.append(d[neighbor])
        
        print(d)
        return d[node]





        