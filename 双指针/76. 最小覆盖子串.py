

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        label = {}
        for k in t:
            if k in label.keys():
                label[k] += 1
            else:
                label[k] = 1
        l = 0
        cnt = 0
        min_l = 0
        min_size = len(s) + 1
        for r in range(len(s)):
            ch = s[r]
            if ch in label:
                label[ch] -= 1
                if label[ch] >= 0:
                    cnt += 1

                while cnt == len(t):
                    if r-l+1 < min_size:
                        min_size = r-l+1
                        min_l = l
                    if s[l] in label:
                        label[s[l]] += 1
                        if label[s[l]] > 0:
                            cnt -= 1
                    l += 1
        return "" if min_size > len(s) else (s[min_l:min_l+min_size])

    def is_match(self, label):
        for v in label.values():
            if v != 0:
                return False
        return True

    def minWindow1(self, s: str, t: str) -> str:
        label = {}
        for c in t:
            if c in label:
                label[c] += 1
            else:
                label[c] = 1

        l = 0
        l_min = 0
        size_min = len(s) + 1
        cnt = 0
        for r in range(len(s)):
            cur_char = s[r]
            if cur_char in label:
                label[cur_char] -= 1

                while self.is_match(label):
                    if r - l + 1 < size_min:
                        size_min = r - l + 1
                        l_min = l
                    if s[l] in label:
                        label[s[l]] += 1
                    l += 1
        return '' if size_min > len(s) else s[l_min:l_min+size_min]






