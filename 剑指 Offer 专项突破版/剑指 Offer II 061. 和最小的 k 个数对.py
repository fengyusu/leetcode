from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        map = {}
        for i in range(m):
            for j in range(n):
                map[i,j] = nums1[i] + nums2[j]

        if m*n < k:
            k = m*n

        res = sorted(map.items(), key=lambda x : x[1])

        return [ [nums1[r[0][0]], nums2[r[0][1]] ] for r in res[:k] ]

sln = Solution()
print(sln.kSmallestPairs([1,1,2], [1,2,3], 9))

