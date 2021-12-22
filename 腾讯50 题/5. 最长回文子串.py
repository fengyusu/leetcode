

class Solution:
    def extend(self, s, n, l, r):
        count = 0

        while l >= 0 and r < n and l <= r and s[l] == s[r]:
            count += 2
            l -= 1
            r += 1

        return count, l+1, r-1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        max_len = 0
        res = None
        for i in range(n-1):
            cur_len, l, r = self.extend(s, n, i, i)
            cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
                res = s[l:r+1]
            cur_len, l, r = self.extend(s, n, i, i+1)
            if cur_len > max_len:
                max_len = cur_len
                res = s[l:r + 1]

        return res

if __name__ == '__main__':
    s = "a"
    solution = Solution()
    result = solution.longestPalindrome(s)
    print(result)
