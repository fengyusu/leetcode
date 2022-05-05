from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates or min(candidates) > target:
            return []

        def dfs(cur_cand):
            if sum(cur_cand) == target:
                cur_cand_ = cur_cand.sort().copy()
                flag = True
                for res_cand in res:
                    if cur_cand_ == res_cand:
                        flag = False
                        break
                if flag:
                    res.append(cur_cand_)
                return
            if sum(cur_cand) > target:
                return

            for c in candidates:
                cur_cand.append(c)
                dfs(cur_cand)
                cur_cand.pop()

        cur_cand = []
        dfs(cur_cand=cur_cand)
        return res


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates or min(candidates) > target:
            return []

        cand_min = min(candidates)

        def dfs(cur_cand):
            if sum(cur_cand) == target:
                res.append(cur_cand.copy())
                return
            if sum(cur_cand) + cand_min > target:
                return

            for c in candidates:
                if not cur_cand or (cur_cand and c >= cur_cand[-1]):
                    cur_cand.append(c)
                    dfs(cur_cand)
                    cur_cand.pop()

        cur_cand = []
        dfs(cur_cand=cur_cand)
        return res

print(tuple([1,2,3]) == tuple([1,3,2]))