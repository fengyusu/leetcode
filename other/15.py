
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                sum = first + nums[l] + nums[r]
                if sum == 0:
                    res.append([first,nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r -1
                    r -= 1
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        # for i in range(len(res)-1, 0, -1):
        #     for j in range(i-1,-1,-1):
        #         if res[i][0] == res[j][0] and res[i][1] == res[j][1] and res[i][2] == res[j][2]:
        #             res.pop(i)
        #             break

        return res

if __name__ == '__main__':
    arr = [-2,0,1,1,2]
    solution = Solution()
    result = solution.threeSum(arr)
    print(result)