"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
 
"""

from typing import List

# bottoms up approach
class Solution:
    def wordBreak(self, s, wordDict):
      s_length = len(s)
      dp = [False] * (s_length + 1)
      dp[s_length] =  True

      for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            word_length = len(word)

            if i + word_length <= s_length and word == s[i: i + word_length]:
                dp[i] = dp[i + word_length]
                if dp[i]:
                    break
    
      return dp[0]

