"""String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters."""

from typing import List

# brute force (o n*M)

def encode(strs: List[str]) -> str:
    string = str()
    for i in range(0, len(strs)):
        for j in range(0, len(strs[i])):
            string += str(ord(strs[i][j]))
            if (j != len(strs[i])-1):
                string += '.'
        if (i != len(strs) - 1):        
            string += ','
    return string

def decode(s: str) -> List[str]:
    stringArr = []
    for item in s.split(','):
        string = str()
        for character in item.split('.'):            
            string += chr(int(character))
        stringArr.append(string)
    return stringArr


# O(n)
def encode2(strs: List[str]) -> str:
    string = str()
    for item in strs:
         string += str(len(item)) + item
    print(string)
    return string

def decode2(s: str) -> List[str]:
    stringArr = []
    first_word_len_index = 0

    while first_word_len_index < len(s) :
        print(first_word_len_index)
        start_slice = first_word_len_index + 1
        end_slice = int(s[first_word_len_index]) + first_word_len_index + 1
        stringArr.append(s[start_slice : end_slice])
        first_word_len_index = end_slice

    return stringArr

print(decode2(encode2(["neet","code","love","you"])))
print(decode2(encode2(["we","say",":","yes"])))
    
