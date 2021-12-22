from typing import List
import random

class Solution:
    def partition(self, nums, l, r):
        pivot_index = random.randint(l,r)
        nums[pivot_index], nums[l] = nums[l],nums[pivot_index]
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l
    def quickSort(self, nums, l, r):
        if l < r:
            pivot = self.partition(nums, l, r)
            self.quickSort(nums, l, pivot-1)
            self.quickSort(nums, pivot+1, r)

    def sortArray0(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        self.quickSort(nums, 0, n-1)
        return nums


    def heapify(self, nums, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r
        if i != largest:
            nums[i],nums[largest] = nums[largest],nums[i]
            self.heapify(nums, largest)


    def buildheap(self, nums):
        for i in range(n // 2):
            self.heapify(nums, i)

    def sortArray(self, nums: List[int]) -> List[int]:
        global n
        n = len(nums)
        self.buildheap(nums)
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            n -= 1
            self.heapify(nums, 0)
        return nums

















