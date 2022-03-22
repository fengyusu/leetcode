from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = 0
        pre_sum_cnt = {pre_sum:1}
        for num in nums:
            pre_sum += num
            res += pre_sum_cnt.get(pre_sum-k, 0)
            pre_sum_cnt[pre_sum] = pre_sum_cnt.get(pre_sum, 0) + 1
        return res
