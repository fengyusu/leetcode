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
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = Uf(n)

        def check(a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                if uf.is_connect(i, j):
                    continue
                if check(strs[i], strs[j]):
                    uf.connect(i, j)

        res = sum([1 for i in range(n) if uf.f[i] == i])
        return res

sln = Solution()
print(sln.numSimilarGroups())


