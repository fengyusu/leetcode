from typing import List

class Solution:
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

    def maximalRectangle(self, matrix: List[str]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0]*m for i in range(n)]
        max_area = 0
        for i in range(m):
            cur_row = matrix[i]
            cur_ones_num = 0
            for j in range(n):
                if cur_row[j] == '0':
                    cur_ones_num = 0
                    left[j][i] = 0
                else:
                    cur_ones_num += 1
                    left[j][i] = cur_ones_num
        for k in range(n):
            max_area = max(max_area, self.largestRectangleArea(left[k]))

        return max_area
