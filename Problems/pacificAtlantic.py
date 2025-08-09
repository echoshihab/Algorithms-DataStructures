"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea
 level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height
 is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and 
Atlantic oceans.

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

import collections
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS = len(heights)
        COLS = len(heights[0])


        pacific, atlantic = set(), set()


        def dfs(row, column, visitSet,  prevHeight):
            if (row, column) in visitSet or row < 0 or column < 0 or row == ROWS or column == COLS or heights[row][column] < prevHeight:
                return
            
            visitSet.add((row,column))

            dfs(row + 1, column, visitSet, heights[row][column])
            dfs(row - 1, column, visitSet, heights[row][column])
            dfs(row, column + 1, visitSet, heights[row][column])
            dfs(row, column - 1, visitSet, heights[row][column])

        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS-1, col,atlantic, heights[ROWS-1][col])

        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS -1 , atlantic, heights[row][COLS - 1])
    
        return list(pacific & atlantic)


class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

            ROWS = len(heights)
            COLS = len(heights[0])

            pacific, atlantic = set(), set()
        
            
            for col in range(COLS):
                pacific.add((0, col))
                atlantic.add((ROWS - 1, col))


            for row in range(ROWS):
                pacific.add((row, 0))
                atlantic.add((row, COLS -1))

            
            def bfs(starting_values, visited):
                queue = collections.deque(starting_values)

                while queue:
                    r,c  = queue.popleft()
                    for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visited or heights[nr][nc] < heights[r][c]:
                            continue
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                
                return visited
            

            
            pacific_visited = bfs(pacific, pacific)
            atlantic_visited = bfs(atlantic, atlantic)
        
            return list(pacific_visited & atlantic_visited)
            