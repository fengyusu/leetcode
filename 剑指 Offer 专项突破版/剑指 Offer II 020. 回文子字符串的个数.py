
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def helper(l,r):
            cnt = 0
            while l <= r and l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt

        for i in range(n):
            res += helper(i,i)
            res += helper(i,i+1)
        return res

