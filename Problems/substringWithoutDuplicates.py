"""
Longest Substring Without Duplicates
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.

"""

#O(n) time complexity
def lengthOfLongestSubstring(s: str) -> int:
    uniqueChars = set()
    l = 0
    max_length = 0

    for r in range(len(s)):
        while s[r] in uniqueChars:
            uniqueChars.remove(s[l])
            l += 1
        uniqueChars.add(s[r])
        max_length = max(max_length, (r - l + 1))
    
    return max_length



print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))

print(lengthOfLongestSubstring("bbbbb"))
        
