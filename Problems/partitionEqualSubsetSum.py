"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1 or sum(nums) % 2: 
            return False
                
        
        target = sum(nums) // 2
        sum_set = set()
        sum_set.add(0)

        for i in range(len(nums) -1 , -1 , -1):
            
            curr_sum_set = set()
            for j in sum_set:
                if target - j == nums[i]:
                    return True               
                curr_sum_set.add(nums[i]+j)
                curr_sum_set.add(j) # don't loose original values at each iteration of sum_set

            sum_set = curr_sum_set
        
        return False



