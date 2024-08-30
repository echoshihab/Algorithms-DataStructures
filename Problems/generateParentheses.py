"""
Generate Parentheses
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7
"""

from typing import List


def generateParenthesis(n: int) -> List[str]:
 ## rules - left or right brace count cannot be greater than n
 ## right brace can only be added if number of left brace is greater than number of right brace
    arr = []
    def backtrack(left, right, result):
        #base case
        if left == n and right == n:        
            arr.append(result)
            return
        
        if left < n:
            backtrack(left+1, right, f'{result}(')

        if right < left:    
            backtrack(left, right+1, f'{result})' )

    backtrack(0, 0, '')
    return arr


print(generateParenthesis(3))


