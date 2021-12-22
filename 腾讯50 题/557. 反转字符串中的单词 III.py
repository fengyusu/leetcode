
class Solution:
    def reverseWord(self, s, l, r):
        while l <= r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
    def reverseWords(self, s: str) -> str:
        sl = list(s)
        l = r = 0
        n = len(sl)
        for i in range(n+1):
            if  i == n or s[i] == ' ':
                r = i - 1
                self.reverseWord(sl, l, r)
                l = i + 1
        return ''.join(sl)