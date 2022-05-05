import collections
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        if n == 1:
            return words[0]

        in_degree = collections.defaultdict(int)
        for word in words:
            for c in word:
                if c not in in_degree:
                    in_degree[c] = 0

        rank_edges = collections.defaultdict(list)


        prev_word = words[0]
        for i in range(1, n):
            cur_word = words[i]
            len0 = len(prev_word)
            len1 = len(cur_word)
            while len0 and len1:
                cur_char = cur_word[-len1]
                prev_char = prev_word[-len0]
                if cur_char != prev_char:
                    if cur_char not in rank_edges[prev_char]:
                        rank_edges[prev_char].append(cur_char)
                        in_degree[cur_char] += 1
                    break
                len0 -= 1
                len1 -= 1
            if len0 > 0 and len1 == 0:
                return ""
            prev_word = cur_word

        print("in_degree ", in_degree)
        print("rank_edges ", rank_edges)

        q = collections.deque([u for u in in_degree.keys() if in_degree[u] == 0])
        res = []
        while q:
            cur_node = q.popleft()
            res.append(cur_node)
            for v in rank_edges[cur_node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if len(res) != len(in_degree):
            res = []
        return "".join(res)

# sln = Solution()
# print(sln.alienOrder(["wnlb"]))

