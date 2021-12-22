
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        count  = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                l = i
                r = i+1
                sl = s[l]
                sr = s[r]
                while l >= 0 and r < len(s) and s[l] == sl and s[r] == sr:
                    count += 1
                    l -= 1
                    r += 1
        return count

    def countBinarySubstrings1(self, s: str) -> int:
        pre = 0
        cur = 1
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            if pre >= cur:
                count += 1
        return count

if __name__ == '__main__':
    arr = "00110011"
    solution = Solution()
    result = solution.countBinarySubstrings1(arr)
    print(result)


