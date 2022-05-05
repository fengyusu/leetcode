import collections
from typing import List

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        n = len(org)
        indegree = {i:0 for i in range(1,n+1)}
        edges = collections.defaultdict(list)
        num_set = set([i for i in range(1,n+1)])

        for seq in seqs:
            pre_seq_num = seq[0]
            if seq[0] not in indegree:
                return False
            if seq[0] in num_set:
                num_set.remove(seq[0])

            for i in range(1, len(seq)):

                if seq[i] not in indegree or seq[i] in seq[:i]:
                    return False
                if seq[i] in num_set:
                    num_set.remove(seq[i])

                if seq[i] not in edges[pre_seq_num]:
                    edges[pre_seq_num].append(seq[i])
                    indegree[seq[i]] += 1

                pre_seq_num = seq[i]
            # print("seq ", seq)

        print("edges ", edges)
        print("indegree ", indegree)

        if len(num_set) != 0:
            return False

        cur_ord_index = 0
        q = collections.deque([i for i in indegree if indegree[i]==0 ])
        if len(q) != 1:
            return False
        print("edges ", edges)
        print("indegree ", indegree)

        visited_seq = []

        while q:
            print("q ", q)
            if len(q) != 1:
                return False
            cur_seq_num = q.popleft()
            visited_seq.append(cur_seq_num)
            if cur_ord_index >= n or cur_seq_num != org[cur_ord_index]:
                return False
            cur_ord_index += 1
            # print("cur_ord_index ", cur_ord_index)

            for neighbor in edges[cur_seq_num]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)



        return True if len(visited_seq) == len(indegree) else False

sln = Solution()
print(sln.sequenceReconstruction([1,2,3,4],
[[1,2,3],[3,4],[4,3]]))

