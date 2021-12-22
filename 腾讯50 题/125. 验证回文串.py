
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        return new_s == new_s[::-1]