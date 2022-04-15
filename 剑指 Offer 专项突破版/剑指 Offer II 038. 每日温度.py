import collections
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(n):
            cur_greater = 0
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    cur_greater = j-i
                    break
            res.append(cur_greater)
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            cur_temp = temperatures[i]
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_index =stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res

sln =   Solution()
print(sln.dailyTemperatures([73,74,75,71,69,72,76,73]))