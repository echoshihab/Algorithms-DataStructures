"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length"""

#O(26n) -> O(n)
def characterReplacement(s: str, k: int) -> int:
    char_counter = {}

    l = 0
    result = 0

    for r in range(len(s)):
        char_counter[s[r]] = 1 + char_counter.get(s[r], 0)

        window_length = r-l + 1
        max_frequency = max(char_counter.values())

        if window_length - max_frequency > k:
            char_counter[s[l]] -= 1
            l +=1
            

        result = max(result, r - l + 1)
    
    return result


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))



#O(26n) -> O(n)
def characterReplacement2(s: str, k: int) -> int:
    char_counter = {}

    l = 0
    result = 0
    max_frequency = 0

    for r in range(len(s)):
        char_counter[s[r]] = 1 + char_counter.get(s[r], 0)
        max_frequency = max(max_frequency, char_counter.get(s[r]))

        window_length = r-l + 1

        if window_length - max_frequency > k:
            char_counter[s[l]] -= 1
            l +=1
            
        result = max(result, r - l + 1)
    
    return result


print(characterReplacement2("ABAB", 2))
print(characterReplacement2("AABABBA", 1))