from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def get_candidates(s, index):
            candidate_ips = [[s[index], index+1]]
            if s[index] != '0':
                for i in range(index+1, max(index+3,n)):
                    if s[index:i+1].isdigit() and int(s[index:i+1]) <= 255:
                        candidate_ips.append([s[index:i+1], i+1])
            return candidate_ips


        def dfs(cur_cand, cur_index):
            if len(cur_cand) == 4 or cur_index >= n:
                if len(cur_cand) == 4 and cur_index == n:
                    res.append(".".join(cur_cand))
                return

            candidate_ips = get_candidates(s, cur_index)
            print(cur_index, candidate_ips)
            for candidate_ip in candidate_ips:
                cur_cand.append(candidate_ip[0])
                dfs(cur_cand, candidate_ip[1])
                cur_cand.pop()

        cur_cand = []
        dfs(cur_cand, 0)
        return res

sln = Solution()
print(sln.restoreIpAddresses("1111"))