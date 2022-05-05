import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        nodes = set()
        edges = collections.defaultdict()
        for i, e in enumerate(equations):
            nodes.add(e[0])
            nodes.add(e[1])
            if e[0] not in edges:
                edges[e[0]] = {}
            edges[e[0]][e[1]] = values[i]
            if e[1] not in edges:
                edges[e[1]] = {}
            edges[e[1]][e[0]] = 1.0 / values[i]

        print("nodes ", nodes)
        print("edges ", edges)


        def dfs(start, target, cur_val, visited):
            print(start, target, cur_val)
            if start == target:
                return cur_val


            if start in edges:
                for k in edges[start]:
                    if k not in visited:
                        visited.append(k)
                        cur_res = dfs(k, target, cur_val * edges[start][k], visited)
                        if cur_res != -1:
                            return cur_res

            return -1

        for query in queries:
            if query[0] not in nodes or query[1] not in nodes:
                res.append(-1.0)
            else:
                print(query)
                visited = [query[0]]
                res.append(dfs(query[0], query[1], 1.0, visited))

        return res


sln = Solution()
print(sln.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x2","x4"]]
))




