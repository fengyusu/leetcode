from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        min_val = min(candidates)
        if not candidates or target < min_val:
            return []
        res = []
        candidates.sort()
        candidates_freq = []
        for candidate in candidates:
            if not candidates_freq or candidate != candidates_freq[-1][0]:
                candidates_freq.append([candidate,1])
            else:
                candidates_freq[-1][1] += 1
        n = len(candidates_freq)

        def dfs(cur_res, level):
            cur_res_sum = sum(cur_res)
            if cur_res_sum == target:
                res.append(cur_res.copy())
                return
            if level <= 0 or cur_res_sum + min_val > target:
                return

            cur_cand = candidates_freq[level - 1]
            for i in range(cur_cand[1] + 1):
                cur_res += [cur_cand[0]] * i
                dfs(cur_res, level-1)
                cur_res = cur_res[:len(cur_res)-i]


        cur_res = []
        dfs(cur_res, n)
        return res


