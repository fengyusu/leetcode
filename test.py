import random


def upper_bound(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return low


def lower_bound(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        print(low, high)
        mid = low + (high - low) // 2
        if nums[mid] == target:
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return high


