
class Solution:
    def moveZeroes(self, nums) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[k] = nums[i]
                k += 1
        for j in range(k,len(nums)):
            nums[j] = 0

if __name__ == '__main__':
    arr = [2,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(arr)
    print(arr)