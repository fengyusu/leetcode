from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.combine = [0]*k
        self.backtracking(pos=1, com_index=0, n=n, k=k)
        return self.res

    def backtracking(self, pos, com_index, n, k):
        if com_index == k:
            self.res.append(self.combine.copy())
            return

        for i in range(pos, n+1):
            self.combine[com_index] = i
            com_index += 1
            self.backtracking(i+1, com_index, n, k)
            com_index -= 1