"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

# O(n) 2 loops 
def isPalindrome(s: str) -> bool:
    cleaned_s = str()    
    for char in s:
        if char.isalnum():
            cleaned_s += char.lower()
    
    result = True

    for i in range(len(cleaned_s)):
        if (cleaned_s[i] != cleaned_s[len(cleaned_s) -1 -i]):            
            result = False
            break

    return result

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
        

#O(n) without extra memory usage            
def isPalindrome2(s: str) -> bool:
    frontIndex = 0
    backIndex = len(s) - 1
    while frontIndex < backIndex:
        while s[frontIndex].isalnum() != True and frontIndex < backIndex:
            frontIndex +=1
        while s[backIndex].isalnum() != True and backIndex > frontIndex:
            backIndex -= 1
        if s[frontIndex].lower() != s[backIndex].lower():
            return False
        frontIndex += 1
        backIndex -= 1 
    return True

print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome2("race a car"))
print(isPalindrome2(".,"))