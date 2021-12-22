

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j = 0

        if j == len(needle):
            return i-j

        return -1

    def getNext(self, s):
        n = len(s)
        next = [0] * n
        next[0] = -1
        k = -1
        j = 0
        while j < n-1:
            if k == -1 or s[k] == s[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next


    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == 0 or len(needle) == 0:
            return 0
        i = 0
        j = 0
        next = self.getNext(needle)
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i-j
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"



    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)
