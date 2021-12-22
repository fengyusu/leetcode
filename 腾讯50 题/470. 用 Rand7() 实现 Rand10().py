
class Solution:
    def rand10(self):
        row = 0
        col = 0
        idx = 0
        row = rand7()
        col = rand7()
        idx = col + (row - 1) * 7
        if idx <= 40:
            return 1 + (idx - 1) % 10
        else:
            while idx > 40:
                row = rand7()
                col = rand7()
                idx = col + (row - 1) * 7
            return 1 + (idx - 1) % 10