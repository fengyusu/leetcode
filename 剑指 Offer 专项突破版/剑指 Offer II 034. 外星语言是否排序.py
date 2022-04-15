from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i in range(26):
            order_map[order[i]] = i

        for i in range(len(words) - 1):
            w1, w1_l = words[i], len(words[i])
            w2, w2_l = words[i + 1], len(words[i + 1])
            for j in range(max(w1_l, w2_l)):
                w1_j = -1 if j >= w1_l else order_map[w1[j]]
                w2_j = -1 if j >= w2_l else order_map[w2[j]]
                if w1_j > w2_j:
                    return False
                if w1_j < w2_j:
                    break
        return True


