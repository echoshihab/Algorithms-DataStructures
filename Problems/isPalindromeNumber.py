"""
given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:

-231 <= x <= 231 - 1
 
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        reversed_num = 0
        original = x

        while original > 0:
            reversed_num = reversed_num * 10 + (original % 10)
            original //= 10
        
        return x == reversed_num


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0): return False

        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10
        
        return x == reversed_num or x == reversed_num // 10
            