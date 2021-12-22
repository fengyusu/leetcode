from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            cur = nums[i] if nums[i] > 0 else -nums[i]
            if nums[cur-1] < 0:
                res.append(cur)
            nums[cur - 1] = -abs(nums[cur -1])
        return res

if __name__ == '__main__':
    arr = [4,3,2,7,8,2,3,1]

    solution = Solution()
    result = solution.findDuplicates(arr)
    print(result)