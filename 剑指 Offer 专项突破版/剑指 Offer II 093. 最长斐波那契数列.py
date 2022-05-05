from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        dp = [{} for i in range(n)]

        max_len = 0

        for i in range(1, n):
            for j in range(0, i):
                diff = arr[i] - arr[j]
                # print("diff ",  diff, dp[j])
                if diff not in dp[j]:
                    dp[i][arr[j]] = 2
                else:
                    dp[i][arr[j]] = dp[j][diff] + 1
                    max_len = max(max_len, dp[i][arr[j]])

            print(arr[i], dp[i])

        return max_len

sln = Solution()
print(sln.lenLongestFibSubseq(
[1,3,4,7,10,11,12,18,23,35]))