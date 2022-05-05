import random
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map.setdefault(nums[i], 0)
            map[nums[i]] += 1

        sorted_map_items = sorted(map.items(), key=lambda x:x[1], reverse=True)
        return [sorted_map_items[i][0] for i in range(k)]

    def pivot(self, nums, left, right):
        rand_index = random.randint(left, right)
        pivot_val = nums[rand_index]
        nums[rand_index], nums[left] = nums[left], nums[rand_index]
        while left < right:
            while left < right and nums[right][1] <= pivot_val[1]:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left][1] >= pivot_val[1]:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot_val
        return left

    def quick_sort(self, nums, left, right, res, k):
        if left <= right:
            pivot_index = self.pivot(nums, left, right)
            print(pivot_index)
            print("nums ", nums)

            if pivot_index <= k - 1:
                for i in range(left, pivot_index + 1):
                    res.append(nums[i][0])
                self.quick_sort(nums, pivot_index + 1, right, res, k)
            else:
                self.quick_sort(nums, left, pivot_index - 1, res, k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map.setdefault(nums[i], 0)
            map[nums[i]] += 1

        res = []
        map_nums = [[k, map[k]] for k in map]
        print(map_nums)
        self.quick_sort(map_nums, 0, len(map) - 1, res, k)
        return res

