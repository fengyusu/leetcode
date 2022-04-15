
class Solution:
    def helper(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        for i in range(n // 2):
            if s[i] != s[n-i-1]:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        self.used_times = 1
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n-i-1]:
                return self.helper(s[i+1:n-i]) or self.helper(s[i:n-i-1])
        return True