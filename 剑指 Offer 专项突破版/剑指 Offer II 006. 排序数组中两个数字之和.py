from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        cur_sum = numbers[l] + numbers[r]
        while l < r and cur_sum != target:
            if cur_sum < target:
                l += 1
            else:
                r -= 1
            cur_sum = numbers[l] + numbers[r]
        return [l,r]
