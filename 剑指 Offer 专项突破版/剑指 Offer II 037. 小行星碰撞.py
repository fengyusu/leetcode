from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n <= 1:
            return asteroids
        res = []
        for i in range(n):
            if len(res) == 0:
                res.append(asteroids[i])
            else:
                cur_asteroid = asteroids[i]
                while not (len(res) == 0 or cur_asteroid*res[-1] >= 0 or (res[-1] < 0 and cur_asteroid > 0)):
                    neighbor_asteroid = res.pop()
                    if abs(cur_asteroid) < abs(neighbor_asteroid):
                        cur_asteroid = neighbor_asteroid
                    elif abs(cur_asteroid) == abs(neighbor_asteroid):
                        cur_asteroid = 0
                res.extend([cur_asteroid] if cur_asteroid else [])
        return res





