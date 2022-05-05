from typing import List


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []

        def dfs(cur_node, cur_path):
            if cur_path and cur_path[-1] == n - 1:
                res.append(cur_path.copy())

            for next_node in graph[cur_node]:
                cur_path.append(next_node)
                dfs(next_node, cur_path)
                cur_path.pop()

        cur_node = 0
        cur_path = [0]
        dfs(cur_node, cur_path)
        return res
