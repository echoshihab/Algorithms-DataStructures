"""
You are given a 
m x n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}



"""

from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])

        visited = set()
        queue = deque()

        
        for row in range(ROWS):
            for column in range(COLS):
                if rooms[row][column] == 0:
                    visited.add((row, column))
                    queue.append((row, column))



        def bfs(r, c):
            if r >= len(rooms) or r < 0 or c >= len(rooms[0]) or c < 0 or (r,c) in visited or rooms[r][c] == -1:
                return
            visited.add((r,c))
            queue.append((r,c))


        
        dist = 0

        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()

                rooms[row][column] = dist

                bfs(row + 1, column)
                bfs(row - 1, column)
                bfs(row, column + 1)
                bfs(row, column - 1)
            
            dist += 1








