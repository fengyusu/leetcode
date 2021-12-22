
class Solution:
    def removeElement0(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        nums = nums[0:k]
        return k

    def removeElement(self, nums, val):
        if nums == None or len(nums) == 0:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            while l < r and nums[r] == val:
                r -= 1
            nums[l],nums[r] = nums[r],nums[l]
        if nums[l] == val:
            return l
        else:
            return l+1

if __name__ == '__main__':
    arr = [0,1,2,2,3,0,4,2]
    solution = Solution()
    result = solution.removeElement(arr, 2)
    print(result,arr)