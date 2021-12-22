


class Solution:
    def dfs(self, isConnected, i, visited):
        if visited[i]:
            return
        visited[i] = True
        n = len(isConnected[i])
        for k in range(n):
            if isConnected[i][k]:
                self.dfs(isConnected, k, visited)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        if len(isConnected) == 0:
            return 0
        circles = 0
        n = len(isConnected)
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                circles += 1
                self.dfs(isConnected, i, visited)
        return circles
