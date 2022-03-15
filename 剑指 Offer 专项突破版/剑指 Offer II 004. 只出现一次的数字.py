from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            total = sum([(num>>i)&1 for num in nums])
            if total % 3:
                if i == 31:
                    res -= (1<<31)
                else:
                    res |= (1 << i)
        return res