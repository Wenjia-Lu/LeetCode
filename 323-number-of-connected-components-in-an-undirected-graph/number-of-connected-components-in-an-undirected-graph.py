class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # init each node's parent as itself
        self.size = [1 for _ in range(n)]
        self.components = n
        
    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A != B: # if parents arent the same
            self.components -= 1
            # optimization here: make smaller tree attach to larger tree!
            if self.size[A] < self.size[B]:
                A, B = B, A
            self.parent[B] = A # B is the smaller one
            self.size[A] += self.size[B]
                
    # def find(self, a):
    #     if self.parent[a] == a:
    #         return a
    #     self.parent[a] = self.find(self.parent[a]) # optimization - flatten the tree for search
    #     return self.parent[a]

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]] # grandparent
            a = self.parent[a]
        return a
    
    def getComp(self):
        # return len(set(self.parent))
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u,v)
        
        return dsu.getComp()


        