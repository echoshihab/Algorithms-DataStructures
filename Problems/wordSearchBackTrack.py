"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""

[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

"ABCCED"


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board) , len(board[0])

        def dfs(row, column, index):
            if index == len(word):
                return True
            
            if row < 0 or column < 0 or row >= ROWS or column >= COLS or word[index] != board[row][column]:
                return False
            
            temp = board[row][column]
            board[row][column] = "*"

            res = ( dfs(row + 1, column, index + 1) or
            dfs(row -1, column, index + 1) or
            dfs(row , column + 1, index + 1) or
            dfs(row, column - 1, index + 1))

            board[row][column] = temp

            return res
             
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False




        