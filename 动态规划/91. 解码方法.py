

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        prev = int(s[0])
        if prev == 0:
            return 0
        if n == 1:
            return 1
        dp = [1] * (n+1)
        for i in range(2,n+1):
            cur = int(s[i-1])
            if (prev != 1 and prev != 2) and cur == 0:
                return 0
            if (prev == 1) or (prev == 2 and cur < 7):
                if cur > 0 :
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
            prev = cur
        return dp[n]




print(int('21'))