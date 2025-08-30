"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
"""

from typing import List

#O(n*m) using extra space for visited
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # go through edge of the board, find all 0s
        # when found find all connected 0s
        # make sure that we keep track of the found 0s

        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c):
            if r == ROWS or r < 0 or c < 0 or c == COLS or board[r][c] != 'O' or (r,c) in visited:
                return

            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(COLS):            
            dfs(0, i) #top
            dfs(ROWS-1, i) #bottom

      
            
        for i in range(ROWS):            
            dfs(i, 0) #left
            dfs(i, COLS-1) #right

        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = 'X'



#mark and restore
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # go through edge of the board, find all 0s
        # when found find all connected 0s
        # make sure that we keep track of the found 0s

        ROWS, COLS = len(board), len(board[0])        

        def dfs(r, c):
            if r == ROWS or r < 0 or c < 0 or c == COLS or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for i in range(COLS):            
            dfs(0, i) #top
            dfs(ROWS-1, i) #bottom      
            
        for i in range(ROWS):            
            dfs(i, 0) #left
            dfs(i, COLS-1) #right

        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'