from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums[-k:]
        self.k = k

    def upper_bound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                right = mid - 1
        return left

    def add(self, val: int) -> int:
        insert_index = self.upper_bound(self.nums, val)
        self.nums.insert(insert_index, val)
        self.nums = self.nums[-self.k:]
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)