"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
 

"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        letter_map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        current = ''

        def dfs(index, curr):

            if index >= len(digits):
                result.append(curr)
                return 
            
            letter_map_index = int(digits[index]) - 2
            for j in range(len(letter_map[letter_map_index])):
                curr += letter_map[letter_map_index][j]
                dfs(index + 1, curr)
                curr = curr[:-1]

            if digits:
                dfs(0, current)

        return result
    

    def letterCombinations2(self, digits: str) -> List[str]:
        
        result = []
        conversion = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(index, curr):

            if len(curr) == len(digits):
                result.append(curr)
                return
            
            for c in conversion[digits[index]]:
                dfs(index+1, curr + c)



            
        if digits:
            dfs(0, "")


        return result

    

            


                


