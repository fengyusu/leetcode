from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        if n < 1:
            return [[]]
        if n == 1:
            return [['Q']]

        self.res_p = []
        permute = []
        self.backtracking(n, permute)

        res = []
        for permute in self.res_p:
            cur_res = []
            for i in range(n):
                cur_str = ['.']*n
                cur_str[permute[i]] = 'Q'
                cur_res.append(''.join(cur_str))
            res.append(cur_res)
        return res


    def is_qualify(self, n, permute):
        if len(permute) == 0:
            return True
        cur_column = permute[-1]
        cur_row = len(permute) - 1
        for r in range(cur_row-1, -1 ,-1):
            detla = cur_row - r
            if permute[r] == cur_column:
                return False
            if cur_column-detla >= 0 and permute[r] == cur_column - detla:
                return False
            if cur_column+detla < n and permute[r] == cur_column + detla:
                return False
        return True


    def backtracking(self, n, permute):
        if not self.is_qualify(n, permute):
            return
        if len(permute) == n:
            self.res_p.append(permute.copy())
            return

        for c in range(n):
            permute.append(c)
            self.backtracking(n, permute)
            permute.pop()
