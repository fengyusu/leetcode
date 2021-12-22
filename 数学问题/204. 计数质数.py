from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        res = 0
        prime = [True]*n
        for i in range(2, n):
            if prime[i]:
                res += 1
                j = i*i
                while j < n:
                    prime[j] = False
                    j += i
        return res


