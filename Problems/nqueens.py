"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Constraints:

1 <= n <= 9
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for i in range(n)]
        result = []

        column = set()
        positiveDiag = set()
        negativeDiag = set()

        def backtrack(row):

            if row == n:
                temp = ["".join(row) for row in board]
                result.append(temp)
                return

            for c in range(n):
                if c in column or row - c in positiveDiag or row + c in negativeDiag:
                    continue

                column.add(c)
                positiveDiag.add(row -  c)
                negativeDiag.add(row + c)
                board[row][c] = "Q"

                backtrack(row + 1)

                column.remove(c)
                positiveDiag.remove(row -  c)
                negativeDiag.remove(row + c)
                board[row][c] = "."

        backtrack(0)
        return result

            


                

                
                    







        
