

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s and t[i] not in dict_t:
                dict_s[s[i]] = i + 1
                dict_t[t[i]] = i + 1
            elif s[i] in dict_s and t[i] in dict_t:
                if  dict_s[s[i]] != dict_t[t[i]]:
                    return False
            else:
                return False
        return True