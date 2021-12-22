
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        sign = 1 if x >= 0 else -1
        n = len(s)
        if sign == -1:
            return  False
        if n == 1:
            return True
        l = 0
        r = n-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

