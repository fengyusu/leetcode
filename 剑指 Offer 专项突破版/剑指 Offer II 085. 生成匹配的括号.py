from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        res = []

        def backtrack(cur_cand, l_rest, r_rest):
            if l_rest > n or r_rest > n or r_rest > l_rest:
                return
            if len(cur_cand) == 2*n:
                if l_rest == n and r_rest == n:
                    res.append("".join(cur_cand))
                return

            if l_rest < n:
                l_rest += 1
                cur_cand.append('(')
                backtrack(cur_cand, l_rest, r_rest)
                l_rest -= 1
                cur_cand.pop()

            if r_rest < n:
                r_rest += 1
                cur_cand.append(')')
                backtrack(cur_cand, l_rest, r_rest)
                r_rest -= 1
                cur_cand.pop()

        cur_cand = []
        backtrack(cur_cand, 0, 0)
        return res



