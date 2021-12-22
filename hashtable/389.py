from utils import *
import string
class Solution:
    def findTheDifference(self, s: string, t: string) -> string:
        t_dict = {}
        for i in t:
            if i not in t_dict.keys():
                t_dict.setdefault(i,1)
            else:
                t_dict[i] = t_dict[i] + 1
        for j in s:
            t_dict[j] = t_dict[j] - 1
        for k in t_dict.keys():
            if t_dict[k] > 0:
                return k


if __name__ == '__main__':
    str = "ba"
    str1 = "bba"
    solution = Solution()
    result = solution.findTheDifference(str,str1)
    print(result)
