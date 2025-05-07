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
        nums.sort()

        def dfs(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            
            current.append(nums[index])
            dfs(index+1, current)
            
            last_elem = current.pop()
            while index + 1 < len(nums) and nums[index + 1] == last_elem:
                index = index + 1

            dfs(index + 1, current)

        
        dfs(0, [])

        return result