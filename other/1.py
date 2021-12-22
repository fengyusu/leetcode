

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lens = len(nums)
        for i in range(lens-1):
            for j in range(i+1, lens):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        return []

    def twoSum0(self, nums: list[int], target: int) -> list[int]:
        lens = len(nums)
        j = -1
        for i in range(lens):
            num2 = target - nums[i]
            if num2 in nums:
                if (nums.count(num2) == 1 and num2 == nums[i]):
                    continue
                else:
                    j = nums.index(num2, i + 1)
                    break
        if j > 0:
            return [i, j]
        else:
            return []
