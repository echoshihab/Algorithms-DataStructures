
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

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     list_output = []
#     for i in range(0, len(strs)):
#         inner_item = [strs[i]]
#         print(inner_item)
#         for j in range(i+1, len(strs)):            
#             if len(inner_item[0]) == len(strs[j]) and len(set(inner_item[0] + strs[j])) == len(inner_item[0]):                
#                 inner_item.append(strs[j])
#         list_output.append(inner_item)        
#     return list_output


# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# O(n ^ 2 * n log)
def groupAnagrams2(strs: List[str]) -> List[List[str]]:
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
                        
    

print(groupAnagrams2(["",""]))
print(groupAnagrams2(["","b"]))
print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams2(["hhhhu","hhhuh"]))
print(groupAnagrams2(["","",  ""]))




        
