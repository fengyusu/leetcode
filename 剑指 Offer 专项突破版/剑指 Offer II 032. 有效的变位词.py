


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        if len(s) != len(t) or s == t:
            return False
        for i in range(len(s)):
            table[ord(s[i]) - ord('a')] += 1
            table[ord(t[i]) - ord('a')] -= 1
        return True if not any(table) else False
