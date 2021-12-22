from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                res.append(product // nums[i])
            else:
                cur_product = 1
                for j in range(n):
                    if i != j:
                        cur_product *= nums[j]
                res.append(cur_product)

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        R = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i]*R
            R *= nums[i]
        return res