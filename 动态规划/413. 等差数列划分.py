
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0]*n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)


if __name__ == '__main__':
    arr = [1,2,3,4,6,7,8]
    solution = Solution()
    res = solution.numberOfArithmeticSlices(arr)
    print("res", res)