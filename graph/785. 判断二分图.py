from collections import deque

class Solution:
    def isBipartite(self, graph) -> bool:
        n = len(graph)
        if n == 0:
            return True

        color = [0] * n
        queue =deque()
        for i in range(n):
            if color[i] == 0:
                queue.append(i)
                color[i] = 1
            while len(queue) != 0:
                node = queue.popleft()
                # print("ndoe ", node, color[node])
                for adj in graph[node]:
                    if color[adj] == 0:
                        color[adj] = 1 if color[node] == 2 else 2
                        queue.append(adj)
                    elif color[adj] == color[node]:
                        return False

        return True

if __name__ == '__main__':
    arr = [[1,3],[0,2],[1,3],[0,2]]

    solution = Solution()
    result = solution.isBipartite(arr)
    print(result,arr)