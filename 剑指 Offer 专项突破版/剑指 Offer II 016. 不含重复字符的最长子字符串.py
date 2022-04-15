
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        win = []
        for c in s:
            if c in win:
                l_index = win.index(c)
                win = win[l_index + 1:]
            win.append(c)
            max_len = max(max_len, len(win))
        return max_len