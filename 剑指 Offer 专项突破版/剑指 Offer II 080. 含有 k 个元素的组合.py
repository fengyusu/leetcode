from typing import List

class Solution:



    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        res = []
        def dfs(level, cur):

            if len(cur) == k:
                res.append(cur.copy())
                return
            if level > n:
                return


            dfs(level + 1, cur)
            cur.append(level)
            dfs(level + 1, cur)
            cur.pop()

        cur = []
        dfs(level=1, cur=cur)
        return res
