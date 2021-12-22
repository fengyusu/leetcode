from typing import List


class Solution:
    def lcp(self, str1, str2):
        l = min(len(str1), len(str2))
        i = 0
        while i < l and str1[i] == str2[i]:
            i += 1
        return str1[:i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prev = strs[0]
        length = len(strs)
        for i in range(1, length):
            prev = self.lcp(prev, strs[i])
            if not prev:
                return ""

        return prev
