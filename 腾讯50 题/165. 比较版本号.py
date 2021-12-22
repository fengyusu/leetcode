

class Solution:
    def parseVersion(self, version:str):
        res = []
        n = len(version)
        l = 0
        for i in range(n):
            if version[i] != '.':
                continue
            res.append(int(version[l:i]))
            l = i+1
        res.append(int(version[l:]))
        return res

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.parseVersion(version1)
        v2 = self.parseVersion(version2)
        print(v1)
        print(v2)
        l1 = len(v1)
        l2 = len(v2)
        n = min(l1,l2)
        for i in range(n):
            if v1[i] == v2[i]:
                continue
            if v1[i] < v2[i]:
                return -1
            else:
                return 1
        if l1 == l2:
            return 0
        elif l1 < l2:
            for i in range(n, l2):
                if v2[i]:
                    return -1
            return 0
        else:
            for i in range(n, l1):
                if v1[i]:
                    return 1
            return 0

if __name__ == '__main__':
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    solution = Solution()
    result = solution.compareVersion(version1, version2)
    print(result)