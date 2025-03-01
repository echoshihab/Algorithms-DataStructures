"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

def checkInclusion(s1: str, s2: str) -> bool:
    s1_tracker = {}

    for letter in s1:
        s1_tracker[letter] = s1_tracker.get(letter, 0) + 1
    print(s1_tracker)

    s1_len = len(s1)
   
    
    for l in range(len(s2)):
        mini_tracker = {}
        if s2[l] in s1_tracker:            

            r = l
            while r - l + 1 <= s1_len and r < len(s2):               
              if s2[r] in s1_tracker:
                    mini_tracker[s2[r]] = (mini_tracker.get(s2[r], 0) + 1)
                    if mini_tracker[s2[r]] > s1_tracker[s2[r]]:
                        mini_tracker = {}
                        break
                    r += 1
              else:
                  break
                  
            
        if mini_tracker == s1_tracker:
            return True
    return False

    


        
    
        
     
    
# print(checkInclusion("ab", "eidbaooo"))
# print(checkInclusion("ab", "eidboaoo"))
# print(checkInclusion("hello", "ooolleoooleh"))
# print(checkInclusion("abcdxabcde", "abcdeabcdx"))
# print(checkInclusion("hello", "ooolleoooleh"))


def checkInclusion2(s1: str, s2: str) -> bool:
    s1_tracker = {}
    s2_tracker = {}

    for letter in s1:
        s1_tracker[letter] = s1_tracker.get(letter, 0) + 1
   
    l = 0
    for r in range(len(s2)):
        s2_tracker[s2[r]] = s2_tracker.get(s2[r], 0) + 1

        if (r - l + 1) > len(s1):
            if s2_tracker[s2[l]] == 1:
                del s2_tracker[s2[l]]
            else:
                s2_tracker[s2[l]] -= 1
            
            l += 1                  
            
        if s2_tracker == s1_tracker:
            return True
    return False

# print(checkInclusion2("abcdxabcde", "abcdeabcdx"))
# print(checkInclusion2("hello", "ooolleoooleh"))


def checkInclusion3(s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        s2_freq = [0]*26
        
        for letter in s1:
            s1_freq[ord(letter) - ord('a')] += 1

        for i in range(len(s2)):
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
            if i >= len(s1):
                s2_freq[ord(s2[i-len(s1)]) - ord('a')] -= 1
            
            if s1_freq == s2_freq:
                return True
        
        return False
        


print(checkInclusion3("hello", "ooolleoooleh"))