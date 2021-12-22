

class Solution:
    def reverse(self, x: int) -> int:
         y = float(0)
         sign = 1
         if x < 0:
            sign = -1
         s = str(abs(x))
         n = len(s)

         for i in range(n):
             y += int(s[i]) * (10**i)

         y = y * sign
         if y >= -2**31 and y < 2**31 - 1:
             return int(y)
         else:
             return 0



