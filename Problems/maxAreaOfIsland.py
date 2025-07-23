"""
You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxIslandArea = 0

        if not grid: 
            return maxIslandArea
        
        def dfs(row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != "1":
                 return 0
            grid[row][column] = "0"

            return ( 1 + 
            dfs(row + 1, column) +
            dfs(row - 1, column) + 
            dfs(row, column + 1) + 
            dfs(row, column - 1))
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    if grid[row][col] == "1":
                        maxIslandArea = max(dfs(row, col), maxIslandArea)
        

        return maxIslandArea




