class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, i):
        i = i - 1
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i
    
    def union(self, a, b): # true means success = diff parents
        A, B = self.find(a-1), self.find(b-1)

        if A != B:
            if self.size[A] < self.size[B]:
                A, B = B, A
            self.parent[B] = A
            self.size[A] += self.size[B]
            return True
        else:
            return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        resU, resV = -1, -1
        for u, v in edges:
            if not dsu.union(u, v): # if union failed aka same group alrdy
                resU, resV = u, v
        
        return [resU, resV]

        