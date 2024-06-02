
from collections import defaultdict
from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""
#brute force

# O(n ^ 2 * n log m)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    rad = []
    hash_map  = {}
    duplicate_checker = []
    for item in strs:
        rad.append("".join(sorted(item)))
        
    for i in range(0, len(strs)):
        if (i not in duplicate_checker):             
            hash_map[strs[i]] = [strs[i]]
            duplicate_checker.append(i)
        for j in range (i + 1, len(strs)):
            if rad[i] == rad[j] and j not in duplicate_checker:
                    hash_map[strs[i]].append(strs[j])
                    duplicate_checker.append(j)

    return hash_map.values()
                        
    

print(groupAnagrams(["",""]))
print(groupAnagrams(["","b"]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["hhhhu","hhhuh"]))
print(groupAnagrams(["","",  ""]))


#o(n * m log m)

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for string in strs:
        sorted_string = ''.join(sorted(string))
        anagram_groups[sorted_string].append(string)
    
    return anagram_groups.values()

print(groupAnagrams2(["",""]))
print(groupAnagrams2(["","b"]))
print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams2(["hhhhu","hhhuh"]))
print(groupAnagrams2(["","",  ""]))


    

         
     

        
