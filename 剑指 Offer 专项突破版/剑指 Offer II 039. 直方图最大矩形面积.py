from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i])
            cur_min_h = heights[i]
            for j in range(i+1,n):
                if heights[j] < cur_min_h:
                    cur_min_h = heights[j]
                    if cur_min_h * (n-i) <= max_area:
                        break
                max_area = max(max_area, cur_min_h * (j-i+1))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = heights[0]
        max_area_map = {heights[0]:heights[0]}
        for i in range(1, n):
            if heights[i] > 0:
                cur_h = heights[i]
                cur_h_max_area_w = 0
                pop_ks = []
                for k in max_area_map:
                    if k < cur_h:
                        cur_max_area = max_area_map[k] + k
                        max_area_map[k] = cur_max_area
                        max_area = max(max_area, cur_max_area)
                    else:
                        cur_h_max_area_w = max(cur_h_max_area_w, max_area_map[k] // k )
                        pop_ks.append(k)
                for k in pop_ks:
                    max_area_map.pop(k)
                max_area_map[cur_h] = cur_h * (1 + cur_h_max_area_w)
                max_area = max(max_area, max_area_map[cur_h])

            else:
                max_area_map = {}
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        left = [0]*n
        right = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_area = max([heights[i] * (right[i]-left[i]-1) for i in range(n)]) if n > 0 else 0
        return max_area






sln = Solution()
print(sln.largestRectangleArea([999,999,999,999]))