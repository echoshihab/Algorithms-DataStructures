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
    # iterative backtracking - n * 2^n
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [i + [num] for i in result]
            print(result)
        return result

    # add recursive backtracking solution - n & 2^n            
    def subsetsDfs(self, nums: List[int]) -> List[List[int]]:
        result = []

        current = []
        def dfs(index: int):
            if index >= len(nums):
                result.append(current.copy())
                return 
            
            current.append(nums[index])
            dfs(index+1)

            current.pop()
            dfs(index+1)


        dfs(0)
        return result
    
        


sol = Solution()
sol.subsets([1,2,3])


