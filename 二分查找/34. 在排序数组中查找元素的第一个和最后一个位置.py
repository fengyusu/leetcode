

class Solution:

    def lower_bound(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

    def upper_bound(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return l

    def searchRange(self, nums, target: int):
        if len(nums) == 0 or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        lower = self.lower_bound(nums, target)
        upper = self.upper_bound(nums, target)
        if nums[lower] != target:
            return [-1, -1]
        return [lower, upper]





if __name__ == '__main__':
    arr = [1,4]
    solution = Solution()
    result = solution.searchRange(arr, 4)
    print(result)