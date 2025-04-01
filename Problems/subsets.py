"""Given an integer array nums of unique elements, return all possible subsets 
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in range(len(nums)):
            j = i
            while j < len(nums):
                if nums[i] == nums[j]:
                    result.append([nums[i]])
                elif len(nums[i:j+1]) > 2:
                    result.append([nums[i], nums[j]])
                    result.append(nums[i:j+1])
                else:
                    result.append([nums[i], nums[j]])
                    
                j += 1
            
        
        return result
            


        