

class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        candys = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candys[i] = max(candys[i], candys[i-1]+1)
        for i in range(n-1,0,-1):
            if ratings[i-1] > ratings[i]:
                candys[i-1] = max(candys[i-1], candys[i]+1)

        return sum(candys)

if __name__ == '__main__':
    arr = [1,0,2]
    solution = Solution()
    result = solution.candy(arr)
    print(result)