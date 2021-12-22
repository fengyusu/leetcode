from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        queue = deque()
        res = []
        indegree = [0 for i in range(numCourses)]
        graph_matrix = [[] for j in range(numCourses)]
        for edge in prerequisites:
            graph_matrix[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        # print(indegree)
        # print(graph_matrix)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.appendleft(i)

        while len(queue) != 0:
            cur = queue.pop()
            res.append(cur)
            for adj in graph_matrix[cur]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.appendleft(adj)

        for i in range(numCourses):
            if indegree[i] != 0:
                return []

        return res




if __name__ == '__main__':
    arr =[[1,0],[2,0],[3,1],[3,2]]

    solution = Solution()
    result = solution.findOrder(4, arr)
    print(result)