"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        ROWS, COLUMNS = len(grid), len(grid[0])

        if COLUMNS == 0:
            return -1

        queue = deque()
        fresh_orange_count = 0
        time  = 0

        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 1:
                    fresh_orange_count +=1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        directions = [(1,0), (-1, 0),(0,1), (0, -1)]
                    
        while queue and fresh_orange_count > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                  nr,nc = r+dr, c+dc
                  if nr >=  0 and nr < ROWS and nc >= 0 and nc < COLUMNS and grid[nr][nc]== 1:
                      queue.append((nr, nc))
                      grid[nr][nc] = 2
                      fresh_orange_count -= 1
            time += 1
                      
                                                            
        if fresh_orange_count > 0:
            return -1
        return time