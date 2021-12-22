from typing import List


class Solution:
    def singleNumber0(self, nums: List[int]) -> int:
        res = 0
        counts = [0]*32
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(32):
                counts[j] += cur & 1
                cur >>= 1
        for i in range(32):
            if (counts[i] % 2):
                res += 2**i
        return res

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    s = [-4,1,2,1,2]
    solution = Solution()
    result = solution.singleNumber(s)
    print(result)
