"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses 
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without 
alerting the police.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List


#first pass using dfs
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        result = [0]

        def dfs(index, currMax):
            result[0] = max(currMax, result[0])    

            if index >= len(nums):
                return 
            
            oldMax = currMax

            dfs(index+1, oldMax)

            currMax = currMax + nums[index]
            
            dfs(index+2, currMax)
            
        dfs(0, 0)

        return result[0]




            