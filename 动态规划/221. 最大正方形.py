from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for i in range(m)]
        print(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    print("0 ",i,j)
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        print("1 ", i, j)
                    else:
                        min_l = min(dp[i-1][j], dp[i][j-1])
                        if matrix[i-min_l][j-min_l] == '1':
                            dp[i][j] = min_l + 1
                        else:
                            dp[i][j] = min_l
        print(dp)
        max_area = 0
        for i in range(m):
            max_area = max(max_area, max(dp[i]))
        return max_area**2

if __name__ == '__main__':
    arr = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    solution = Solution()
    res = solution.maximalSquare(arr)
    print("res", res)
    # print("test", (max([[0, 0, 0, 1], [1, 1, 0, 1], [1, 2, 1, 1], [0, 1, 2, 2], [0, 1, 2, 3]])))