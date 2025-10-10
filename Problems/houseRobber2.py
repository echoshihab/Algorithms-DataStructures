"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
 All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
 adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1 : return nums[0]

        def robPartial(start, end):
            h1 = h2 = 0
            for i in range(start, end):
                temp = h2
                h2 = max(h1 + nums[i], h2)
                h1 = temp
            return h2

        return max(robPartial(0, len(nums)-1), robPartial(1, len(nums)))


