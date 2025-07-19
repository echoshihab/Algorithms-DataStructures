"""

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandsCount = 0

        if not grid:
            islandsCount

        def bfs(r, c):
            ##right, left, bottom, up
            directions = [[1,0], [-1,0], [0, 1], [0,-1]]
            queue = collections.deque()
            visited.add((r, c))    
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
            
                for dRow, dColumn in directions:
                    r, c = row + dRow, col + dColumn
                    if (r in range(rows) and 
                        c in range(columns) and
                        grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r,c))
        

        
        rows, columns = len(grid), len(grid[0])
        
        visited = set()

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    islandsCount += 1

        return islandsCount