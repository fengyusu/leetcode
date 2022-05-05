from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 1:
            return min(costs[0])

        pre_cost = costs[0]

        for i in range(1,n):
            cur_cost = [0]*3
            cur_cost[0] = min(pre_cost[1], pre_cost[2]) + costs[i][0]
            cur_cost[1] = min(pre_cost[0], pre_cost[2]) + costs[i][1]
            cur_cost[2] = min(pre_cost[0], pre_cost[1]) + costs[i][2]
            pre_cost = cur_cost

        return min(pre_cost)