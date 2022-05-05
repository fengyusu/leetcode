

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0


        flip_map = {'0':0, '1':0}
        if s[0] == '0':
            flip_map['1'] = 1
        else:
            flip_map['0'] = 1

        for i in range(1, n):
            if s[i] == '0':
                flip_0 = flip_map['0']
                flip_1 = min(flip_map['0'], flip_map['1']) + 1
            else:
                flip_0 = flip_map['0'] + 1
                flip_1 = min(flip_map['0'], flip_map['1'])
            flip_map['0'] = flip_0
            flip_map['1'] = flip_1

        return min(flip_map.values())
