from typing import List
class Solution:

    def helper(self, matrix, target, l, r, u, d):
        if l > r or u > d:
            return False
        row = u + (d - u) // 2
        col = l + (r - l) // 2

        if matrix[row][col] == target:
            return True

        if matrix[row][col] > target:
            return self.helper(matrix, target, l, col-1, u, d) or \
                   self.helper(matrix, target, col, r, u, row-1)

        else:
            return self.helper(matrix, target, col+1, r, u, d) or \
                   self.helper(matrix, target, l, col, row+1, d)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m =  len(matrix)
        n = len(matrix[0])
        return self.helper(matrix, target, 0, n-1, 0, m-1)