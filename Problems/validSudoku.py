"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""

from collections import defaultdict
from typing import List

# brute force
def isValidSudoku(board: List[List[str]]) -> bool:
    matched_dict = defaultdict(int)
    is_valid_sudoku = True    

    #check row
    for item in board:
        matched_dict.clear()
        if is_valid_sudoku == False:
            break
        for cell in item:
            if cell == '.':
                continue
            elif cell in matched_dict:
                is_valid_sudoku = False
                break
            else: 
                matched_dict[cell] = 1

    if is_valid_sudoku == False: 
        return is_valid_sudoku

    matched_dict.clear()
    
    # check column
    for item in board:
        index = 0
        matched_dict.clear()
        print(item[index])
        if item[index] == '.':
            index += 1
            continue
        elif item[index] in matched_dict:
            is_valid_sudoku = False
            break
        else:
            index += 1
            matched_dict[item[index]] = 1
    
    print(matched_dict)
    if is_valid_sudoku == False:
        return is_valid_sudoku

    matched_dict.clear()

    nine_by_nine = defaultdict(int)
    #check 3 by 3
    
    nine_by_nine[1] = board[0][0:3] + board[1][0:3] + board[2][0:3]
    nine_by_nine[2] = board[3][0:3] + board[4][0:3] + board[5][0:3]
    nine_by_nine[3] = board[6][0:3] + board[7][0:3] + board[8][0:3]

    nine_by_nine[4] = board[0][3:6] + board[1][3:6] + board[2][3:6]
    nine_by_nine[5] = board[3][3:6] + board[4][3:6] + board[5][3:6]
    nine_by_nine[6] = board[6][3:6] + board[7][3:6] + board[8][3:6]

    nine_by_nine[7] = board[0][6:9] + board[1][6:9] + board[2][6:9]
    nine_by_nine[8] = board[3][6:9] + board[4][6:9] + board[5][6:9]
    nine_by_nine[9] = board[6][6:9] + board[7][6:9] + board[8][6:9]


    for item in nine_by_nine.values():
        if is_valid_sudoku == False:
            break
        matched_dict.clear()
        for cell in item:
            if(cell == '.'):
                continue
            elif cell in matched_dict:
                is_valid_sudoku = False
                break
            else:
                matched_dict[cell] = 1
    
    if is_valid_sudoku == False:
        return is_valid_sudoku

    return is_valid_sudoku

print(
isValidSudoku(
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
)
)




print(isValidSudoku([
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
            


print(isValidSudoku([[".",".","4",".",".",".","6","3","."],
                     [".",".",".",".",".",".",".",".","."],
                     ["5",".",".",".",".",".",".","9","."],
                     [".",".",".","5","6",".",".",".","."],
                     ["4",".","3",".",".",".",".",".","1"],
                     [".",".",".","7",".",".",".",".","."],
                     [".",".",".","5",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".","."]]))            

