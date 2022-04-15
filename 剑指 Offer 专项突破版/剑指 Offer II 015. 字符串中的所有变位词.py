from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        n = len(s)
        if m > n :
            return []
        count_dict = {}
        diff_cnt = 0
        for i in range(m):
            count_dict.setdefault(p[i],0)
            count_dict[p[i]] -= 1
            count_dict.setdefault(s[i], 0)
            count_dict[s[i]] += 1

        for k in count_dict:
            if count_dict[k] != 0:
                diff_cnt += 1

        res = []
        if diff_cnt == 0:
            res.append(0)

        for i in range(m, n):
            if s[i] not in count_dict:
                diff_cnt += 1
                count_dict[s[i]] = 1
            else:
                count_dict[s[i]] += 1
                if count_dict[s[i]]==1 :
                    diff_cnt += 1
                if count_dict[s[i]]==0 :
                    diff_cnt -= 1

            count_dict[s[i-m]] -= 1
            if count_dict[s[i-m]] == 0:
                diff_cnt -= 1
            if count_dict[s[i-m]] == -1:
                diff_cnt += 1
            if diff_cnt == 0:
                res.append(i-m+1)
        return res