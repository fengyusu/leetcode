
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        val_cnt = 0
        cnt_dict = {}
        for c in t:
            cnt_dict.setdefault(c,0)
            cnt_dict[c] -= 1

        l = 0
        min_l = 0
        min_size = len(s)+1
        for r in range(len(s)):
            if s[r] in cnt_dict:
                cnt_dict[s[r]] += 1
                if cnt_dict[s[r]] <= 0:
                    val_cnt += 1

                while val_cnt == len(t):
                    if min_size > r-l+1:
                        min_size = r-l+1
                        min_l = l
                    if s[l] in cnt_dict:
                        cnt_dict[s[l]] -= 1
                        if cnt_dict[s[l]] < 0:
                            val_cnt -= 1
                    l += 1

        return "" if min_size == len(s)+1 else s[min_l:min_l+min_size]



