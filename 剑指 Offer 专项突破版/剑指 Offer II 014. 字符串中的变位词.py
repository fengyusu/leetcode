
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n :
            return False
        count_dict = {}
        diff_cnt = 0
        for i in range(m):
            count_dict.setdefault(s1[i],0)
            count_dict[s1[i]] -= 1
            count_dict.setdefault(s2[i], 0)
            count_dict[s2[i]] += 1

        for k in count_dict:
            if count_dict[k] != 0:
                diff_cnt += 1

        if diff_cnt == 0:
            return True

        for i in range(m, n):
            if s2[i] not in count_dict:
                diff_cnt += 1
                count_dict[s2[i]] = 1
            else:
                count_dict[s2[i]] += 1
                if count_dict[s2[i]]==1 :
                    diff_cnt += 1
                if count_dict[s2[i]]==0 :
                    diff_cnt -= 1

            count_dict[s2[i-m]] -= 1
            if count_dict[s2[i-m]] == 0:
                diff_cnt -= 1
            if count_dict[s2[i-m]] == -1:
                diff_cnt += 1
            if diff_cnt == 0:
                return True
        return False