

class Solution:
    def topKFrequent(self, nums, k: int):
        counts = {}
        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1
        print(counts)
        counts_list = []
        for key in counts:
            counts_list.append((key, counts[key]))
        print(counts_list)
        counts_list.sort(key=lambda x:x[1], reverse=True)
        print(counts_list)
        res_list = []
        for i in range(k):
            res_list.append(counts_list[i][0])
        return res_list

if __name__ == '__main__':
    nums = [4,1,-1,2,-1,2,3]
    solution = Solution()
    res = solution.topKFrequent(nums, 2)
    print(res)