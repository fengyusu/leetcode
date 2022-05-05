import sys
from typing import List

class Solution:
    def upper_bound(self, nums, target):
        low, high = 0, len(nums) - 1
        pos = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:  # >
                high = mid
                pos = high
        if nums[low] > target:
            pos = low
        return pos
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False

        n = len(nums)
        if n <= k+1:
            win_size = n
        else:
            win_size = k+1

        win = nums[:win_size]
        win.sort()

        cur_min_diff = sys.maxsize - 1
        for i in range(win_size-1):
            cur_min_diff = min(cur_min_diff, abs(win[i] - win[i+1]))

        r = len(win)
        while True:
            # print("r ", r)
            # print("win ", win)
            # print("cur_min_diff ", cur_min_diff)

            if cur_min_diff <= t:
                return True

            win.pop(win.index(nums[r-win_size]))
            if r < n:
                # while start_index < len(win) and nums[r] > win[start_index]:
                #     start_index += 1
                start_index = self.upper_bound(win, nums[r])

                win.insert(start_index, nums[r])
                if start_index-1 >= 0 :
                    cur_min_diff = min(cur_min_diff, abs(win[start_index] - win[start_index-1]))
                if start_index+1 < win_size :
                    cur_min_diff = min(cur_min_diff, abs(win[start_index] - win[start_index+1]))

                r += 1
            else:
                break

        return False

sln = Solution()
print(sln.containsNearbyAlmostDuplicate([3,6,0,4],2,2))




