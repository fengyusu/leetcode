from typing import List

class Solution:
    def partition(self, nums, left, right):
        pivot_value = nums[left]
        while left < right:
            while left < right and nums[right] <= pivot_value:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] >= pivot_value:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot_value
        return left

    def find_k(self, nums: List[int], k: int, left, right) -> int:
        if left > right:
            return -1
        pivot = self.partition(nums, left, right)
        if pivot == k-1:
            return nums[pivot]
        elif pivot < k-1:
            return self.find_k(nums, k, pivot+1, right)
        else:
            return self.find_k(nums, k, left, pivot-1)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.find_k(nums, k, 0, len(nums)-1)
