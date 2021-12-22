
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.extendSubstrings(s, i, i)
            count += self.extendSubstrings(s, i, i+1)
        return count

    def extendSubstrings(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count