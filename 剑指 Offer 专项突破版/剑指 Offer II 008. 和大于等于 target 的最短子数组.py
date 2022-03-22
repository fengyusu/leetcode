from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        cur_win_sum = nums[0]
        l = 0
        r = 1
        while r < n:
            while r < n and cur_win_sum < target:
                cur_win_sum += nums[r]
                r += 1

            if cur_win_sum >= target:
                min_len = min(min_len, r - l)

            while l < n and cur_win_sum >= target:
                cur_win_sum -= nums[l]
                l += 1
                if cur_win_sum >= target:
                    min_len = min(min_len, r - l)

        return 0 if min_len > n else min_len

nums = [2,3,1,2,4,3]
sln = Solution()
print(sln.minSubArrayLen(7, nums))