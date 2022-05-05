import collections
from typing import List



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        edges = collections.defaultdict(list)
        for pre in prerequisites:
            edges[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1

        q = collections.deque([u for u in range(numCourses) if in_degree[u] == 0])
        res = []
        while q:
            cur_node = q.popleft()
            res.append(cur_node)
            for v in edges[cur_node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if len(res) != numCourses:
            res = []
        return res
