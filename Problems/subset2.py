"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        result_dict = {}

        def dfs(index, current):
            if index == len(nums):
                temp = current.copy()
                temp.sort()
                temp_key = "".join(str(temp))
                if result_dict.get(temp_key) is None:
                    result.append(current.copy())
                    result_dict[temp_key] = 1
                return
            
            current.append(nums[index])
            dfs(index+1, current)
            
            current.pop()
            dfs(index + 1, current)

        
        dfs(0, [])

        return result