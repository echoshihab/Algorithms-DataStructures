from collections import defaultdict

"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""

#O(n) 
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    hash_map_s = {}
    hash_map_t = {}

    for i in s:
        if i in hash_map_s:
            hash_map_s[i] += 1
        else:
            hash_map_s[i] = 1

    for i in t:
        if i in hash_map_t:
            hash_map_t[i] += 1
        else:
            hash_map_t[i] = 1

    if (hash_map_s == hash_map_t):
        return True
    
    return False

print(isAnagram("rat", "car"))
print(isAnagram("anagram", "nagaram"))


# alternative
def isAnagramAlt(s: str, t: str) -> bool:

    charCountDict = defaultdict(int)

    for letter in s:
        charCountDict[letter] += 1

    for letter in t:
        charCountDict[letter] -= 1

    for val in charCountDict.values():
        if val != 0 :
            return False
        
    return True

    
print(isAnagramAlt("rat", "car"))
print(isAnagramAlt("anagram", "nagaram"))


        