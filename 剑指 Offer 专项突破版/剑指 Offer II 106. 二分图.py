from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        visited = [0]*n

        for i in range(n):
            if visited[i] == 0:
                print(i)
                visited[i] = 1
                queue = deque()
                queue.append(i)
                while queue:
                    cur_node = queue.popleft()
                    cur_color = visited[cur_node]
                    for neighbor in graph[cur_node]:
                        if visited[neighbor] == 0:
                            visited[neighbor] = 2 if cur_color == 1 else 1
                            queue.append(neighbor)
                        else:
                            if visited[neighbor] == cur_color:
                                return False
                    print(cur_node, visited)
        return True

sln = Solution()
print(sln.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
