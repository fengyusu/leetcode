class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        n = len(s)
        r = 0
        res = 0
        for i in range(n):
            if i != 0:
                win.remove(s[i-1])
            while r < n and s[r] not in win:
                win.add(s[r])
                r += 1
            res = max(res,len(win))
        return res

if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
