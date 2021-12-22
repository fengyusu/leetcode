from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num_strs = len(strs)
        dp = [[0] * (n + 1) for j in range(m + 1)]
        for k in range(1, num_strs + 1):
            l0 = strs[k - 1].count('0')
            l1 = strs[k - 1].count('1')
            print(l0,l1)
            for i in range(m, l0-1, -1):
                for j in range(n, l1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - l0][j - l1] + 1)
            # print(k, dp)

        return dp[m][n]



if __name__ == '__main__':
    arr = ["10", "0001", "111001", "1", "0"]

    solution = Solution()
    res = solution.findMaxForm(arr,5,3)
    print("res", res)