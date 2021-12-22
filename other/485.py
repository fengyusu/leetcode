
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        record_max = 0
        current_max = 0
        for i in range(len(nums)):
            if nums[i]:
                current_max += 1
            else:
                if current_max > record_max:
                    record_max = current_max
                current_max = 0
        return max(current_max, record_max)

if __name__ == '__main__':
    arr = [1,1,0,1,1,1]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(arr)
    print(result)