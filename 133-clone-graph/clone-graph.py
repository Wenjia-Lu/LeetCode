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

        d = {node: Node(node.val)}
        q = deque([node])
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(val=neighbor.val)
                    q.append(neighbor)
                d[n].neighbors.append(d[neighbor])
        return d[node]





        