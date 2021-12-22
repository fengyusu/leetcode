from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        visited = [[False]*n for i in range(m)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        dir_index = 0
        cur_pos = (0,-1)
        prev_pos = cur_pos
        for i in range(m*n):
            x = prev_pos[0] + dirs[dir_index][0]
            y = prev_pos[1] + dirs[dir_index][1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                dir_index = (dir_index + 1) % 4
                x = prev_pos[0] + dirs[dir_index][0]
                y = prev_pos[1] + dirs[dir_index][1]
            print("pos", (x,y))
            res.append(matrix[x][y])
            visited[x][y] = True
            prev_pos = (x,y)

        return res

if __name__ == '__main__':
    s = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    solution = Solution()
    result = solution.spiralOrder(s)
    print(result)

