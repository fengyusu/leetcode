from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                l_w = len(w)
                if i >= l_w and s[i-l_w:i] == w:
                    dp[i] = dp[i] or dp[i-l_w]
        return dp[n]
