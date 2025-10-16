"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        tot = 0
        
        for i in range(len(s)):

            #odd get odd substrings - 1 - 3 etc
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tot += 1             
                l -= 1
                r += 1


            #even- get even substrings - 2 - 4 
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tot += 1           
                l -= 1
                r += 1

        return tot