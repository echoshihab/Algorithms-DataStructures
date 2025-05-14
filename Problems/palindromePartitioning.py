"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters."""


from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []


        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i , j):
                    partition.append(s[i : j+1])
                    dfs(j + 1)
                    partition.pop()
            
        dfs(0)
        return result
    

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right -1
        
        return True
                                     



        