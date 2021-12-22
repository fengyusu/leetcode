
class UF:
    def __init__(self, n):
        self.n = n
        self.id = [i for i in range(n)]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connect(self, p, q):
        self.id[self.find(p)] = self.find(q)

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        uf = UF(n+1)
        for i in range(n):
            edge = edges[i]
            if uf.isConnected(edge[0], edge[1]):
                return edge
            uf.connect(edge[0], edge[1])
        return [-1, -1]

