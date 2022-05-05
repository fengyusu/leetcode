from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])

        zero_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]

        q = deque(zero_pos)
        visited = set(zero_pos)
        dist = [[0] * n for i in range(m)]

        level = 1
        while q:
            [i, j] = q.popleft()

            dir = [-1, 0, 1, 0, -1]
            for k in range(4):
                x = i + dir[k]
                y = j + dir[k + 1]
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited:
                    dist[x][y] = dist[i][j] + 1
                    visited.add((x, y))
                    q.append([x, y])

        return dist










