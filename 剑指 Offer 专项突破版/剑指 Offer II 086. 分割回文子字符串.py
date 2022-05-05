from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        f = [[True]*n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        def extend_substrings(s, l):
            cand_substrings = [[s[l],l+1]]
            for i in range(l+1, n):
                if f[l][i]:
                    cand_substrings.append([s[l:i+1], i+1])
            return cand_substrings

        def dfs(cur_cand, cur_index):
            if cur_index == n:
                res.append(cur_cand.copy())
                return

            cand_substrings = extend_substrings(s, cur_index)
            for cand_substring in cand_substrings:
                cur_cand.append(cand_substring[0])
                dfs(cur_cand, cand_substring[1])
                cur_cand.pop()

        cur_cand = []
        dfs(cur_cand, 0)
        return res



