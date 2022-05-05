from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(cur_node):
            visited[cur_node] = True
            for i in range(n):
                if isConnected[cur_node][i] and i != cur_node and not visited[i]:
                    dfs(i)

        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
            print(i, res, visited)


        return res

sln =Solution()
print(sln.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))