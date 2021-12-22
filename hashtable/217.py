from utils import *

class Solution:
    def containsDuplicate0(self, nums) -> bool:
        table = {}
        for num in nums:
            if num not in table.keys():
                table.setdefault(num, 0)
            else:
                return True
        return False

    def containsDuplicate(self, nums) -> bool:
        table = set()
        for num in nums:
            table.add(num)
        if len(table) != len(nums):
            return True
        return False


if __name__ == '__main__':
    arr = [1,2,1,4,5,6]
    solution = Solution()
    result = solution.containsDuplicate(arr)
    print(result)
