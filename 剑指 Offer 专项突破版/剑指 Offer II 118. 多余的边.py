from typing import List


class Uf:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n))

    def find(self, i):
        x = i
        while self.f[x] != x:
            x = self.f[x]
        return x

    def connect(self, i, j):
        self.f[self.find(i)] = self.find(j)

    def is_connect(self, i, j):
        return self.find(i) == self.find(j)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = Uf(n+1)
        for edge in edges:
            if uf.is_connect(edge[0], edge[1]):
                return edge
            uf.connect(edge[0], edge[1])
        return []


