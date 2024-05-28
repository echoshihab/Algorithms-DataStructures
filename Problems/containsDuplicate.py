"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# brute force
# O(n)^2
from typing import List

def containsDuplicateBruteForce(nums: List[int]) -> bool:
    for i in range(0, len(nums)):
        currItem = nums[i]
        for k in range(i + 1, len(nums)):
            if nums[k] == currItem:
                return True
    return False

testArr1 = [1,2,3,4]
testArr2 = [1,1,1,3,3,4,3,2,4,2]

print(containsDuplicateBruteForce(testArr1))
print(containsDuplicateBruteForce(testArr2))


#using hashmap O(n)
def containsDuplicateHashMap(nums: List[int]) -> bool:
    hash_map = {}
    for i in range(0, len(nums)):
        if(nums[i] in hash_map):
            return True
        else:
            hash_map[nums[i]] = nums[i]
    return False

print(containsDuplicateHashMap(testArr1))
print(containsDuplicateHashMap(testArr2))


#using hashmap O(n)
def containsDuplicateHashSet(nums: List[int]) -> bool:
    hash_set = set()
    for num in nums:
        if(num in hash_set):
            return True
        else:
            hash_set.add(num)
    return False

print(containsDuplicateHashSet(testArr1))
print(containsDuplicateHashSet(testArr2))
