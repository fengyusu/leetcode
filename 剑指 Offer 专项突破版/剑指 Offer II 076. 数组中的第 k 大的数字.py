import random
from typing import List

class Solution:

    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        pivot_val = nums[left]
        while left < right:
            while left < right and nums[right] <= pivot_val:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] >= pivot_val:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot_val
        return left

    def quick_sort(self, nums, left, right, k):
        if left <= right:
            pivot = self.partition(nums, left, right)
            if pivot == k-1:
                return nums[pivot]
            elif pivot < k-1:
                return self.quick_sort(nums, pivot+1, right, k)
            elif pivot > k-1:
                return self.quick_sort(nums, left, pivot-1, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(nums, 0, len(nums)-1, k)




    def heapfy(self, nums, i, max_len):
        largest = i
        if i * 2 < max_len:
            largest = i*2 if nums[i*2] > nums[largest] else largest
        if i * 2 + 1 < max_len:
            largest = i*2+1 if nums[i*2+1] > nums[largest] else largest
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapfy(nums, largest, max_len)



    def build_heap(self, nums, max_len):
        if len(nums) >= max_len:
            for i in range(max_len-1, -1, -1):
                self.heapfy(nums, i, max_len)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_len = len(nums)
        if k >= max_len:
            return min(nums)

        self.build_heap(nums, max_len)
        for i in range(k-1):
            nums[0],nums[max_len-1] = nums[max_len-1],nums[0]
            max_len -= 1
            self.heapfy(nums, 0, max_len)
        return nums[0]

