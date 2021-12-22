from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0]) if self.m > 0 else 0
        if len(word) == 0 or self.m == 0:
            return False
        self.find = False
        for x in range(self.m):
            for y in range(self.n):
                visited = [[False]*self.n for _ in range(self.m)]
                if self.backtracking(board, word, x, y, 0, visited):
                    return True
        return self.find

    def backtracking(self, board, word, x, y, w_i, visited):
        if visited[x][y] or self.find or board[x][y] != word[w_i]:
            return
        if w_i == len(word) - 1:
            self.find = True
        visited[x][y] = True
        dir = [-1,0,1,0,-1]
        for k in range(4):
            cur_x = x + dir[k]
            cur_y = y + dir[k+1]
            if cur_x >= 0 and cur_x < self.m and cur_y >= 0 and cur_y < self.n:
                self.backtracking(board, word, cur_x, cur_y, w_i+1, visited)
        visited[x][y] = False
