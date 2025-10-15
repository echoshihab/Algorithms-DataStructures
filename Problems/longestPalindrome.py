"""Given a string s, return the longest palindromic substring in s."""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        result = ''
        resLength = 0


        for i in range(len(s)):
            # odd
            l,r = i,i

            while l >= 0 and r < len(s)  and s[l] == s[r]:
                if r + 1 - l > resLength:
                    result = s[l:r+1]
                    resLength = r + 1 - l
                l -= 1
                r += 1
                
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r + 1 - l > resLength:
                    result = s[l:r+1]
                    resLength = r + 1 - l
                l -= 1
                r += 1

        return result