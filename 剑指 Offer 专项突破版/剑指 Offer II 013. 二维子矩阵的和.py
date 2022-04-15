from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.prefix_sum = [[0]*(self.n+1) for i in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.prefix_sum[i+1][j+1] = self.prefix_sum[i+1][j] + self.prefix_sum[i][j+1] + matrix[i][j] - self.prefix_sum[i][j]
            print(self.prefix_sum[i])





    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2 += 1
        col2 += 1
        return self.prefix_sum[row2][col2] - self.prefix_sum[row1][col2] - self.prefix_sum[row2][col1] + self.prefix_sum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)

param_1 = obj.sumRegion(2,1,4,3)