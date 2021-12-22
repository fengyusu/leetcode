from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        max_len = 1
        pre = 0
        for i in range(1,n):
            if s[i] in s[pre:i]:
                pre = s.index(s[i], pre, i) + 1
            max_len = max(max_len, i - pre + 1)
        return max_len

if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
