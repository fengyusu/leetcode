import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = collections.defaultdict(list)
        for s in strs:
            cur_list_key = list([0]*26)
            for c in s:
                cur_list_key[ord(c) - ord('a')] += 1
            anagrams_map[tuple(cur_list_key)].append(s)
        return list(anagrams_map.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = collections.defaultdict(list)
        for s in strs:
            cur_list_key = "".join(sorted(s))
            anagrams_map[cur_list_key].append(s)
        return list(anagrams_map.values())

sln = Solution()
print(sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))