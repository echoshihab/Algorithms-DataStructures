"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

# O(n) time complexity
def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
        return ""


    counter_t = {}
    counter_window = {}

    for letter in t:
        counter_t[letter] = 1 + counter_t.get(letter, 0)

    have, need = 0, len(counter_t)

    result, resultLength = [-1, -1], float("infinity")
    
    l = 0
    for r in range(len(s)):
        letter = s[r]
        counter_window = 1 + counter_window.get(letter , 0)


        if letter in counter_t and counter_window[letter] == counter_t[letter]:
            have += 1
        
        while have == need:
            if (r - l + 1) < resultLength:
                result  = [l, r]
                resultLength = r -l + 1
            
            # pop from the left of our window
            counter_window[s[l]] -= 1

            if s[l] in counter_t and counter_window[s[l]] < counter_t[s[l]]:
                have -= 1
            
            l += 1
    
    l,r = result

    return s[l: r+1] if resultLength != float("infinity") else ""

