from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        prev_h = min(height[l], height[r])
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                h = height[l]
                while l < r and h >= height[l]:
                    l += 1
            else:
                h = height[r]
                while l < r and h >= height[r]:
                    r -= 1
        return max_area


        return max_area
