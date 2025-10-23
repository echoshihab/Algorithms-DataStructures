"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        memo = {}


        def dfs(index, prev_index):
            if index == n:
                return 0
            
            if (index, prev_index) in memo:
                return memo[(index, prev_index)]
            
            # skip
            skip = dfs(index+1, prev_index)
            
            #include current index
            take = 0
            if prev_index == -1 or nums[index] > nums[prev_index]:
                take = 1 + dfs(index+1, index)
            
            memo[(index, prev_index)] = max(skip, take)
            
            return memo[(index, prev_index)]


        return dfs(0, -1)

        