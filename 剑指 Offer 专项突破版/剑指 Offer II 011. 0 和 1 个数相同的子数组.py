class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_len = 0
        prefix_sum = 0
        prefix_sum_dict = {}
        prefix_sum_dict[0] = -1
        for i in range(n):
            if nums[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in prefix_sum_dict:
                max_len = max(max_len, i - prefix_sum_dict[prefix_sum])
            else:
                prefix_sum_dict[prefix_sum] = i

        return max_len