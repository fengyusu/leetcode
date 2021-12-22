
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 0:
             return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp_max = [0] * n
        dp_max[0] = nums[0]
        dp_max[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp_max[i] = max(dp_max[i - 1], dp_max[i - 2] + nums[i])
        return dp_max[n-1]


