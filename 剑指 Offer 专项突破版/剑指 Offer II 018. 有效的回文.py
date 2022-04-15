
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalize_s = ''.join([c if c.isdigit() or c.isalpha() else '' for c in s]).lower()
        n = len(normalize_s)
        if n <= 1:
            return True
        for i in range(n // 2):
            if normalize_s[i] != normalize_s[n-i-1]:
                return False
        return True


