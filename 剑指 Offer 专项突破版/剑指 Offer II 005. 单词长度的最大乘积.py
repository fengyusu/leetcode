from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                set_i = set(list(words[i]))
                set_j = set(list(words[j]))
                if not (set_i & set_j):
                    res = max(res, len(words[i])*len(words[j]))
        return res