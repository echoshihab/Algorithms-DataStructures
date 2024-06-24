"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

from collections import defaultdict
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and [nums[i]] == nums[i-1]:
            continue
        left_index = i+1
        right_index = len(nums) - 1
        while left_index < right_index:
            three_sum =  nums[i] + nums[left_index] + nums[right_index]
            if three_sum > 0 :
                right_index -= 1
            elif three_sum < 0:
                left_index += 1
            else:
                result.append([nums[i], nums[left_index], nums[right_index]])
                left_index += 1
                while nums[left_index] == nums[left_index -1] and left_index < right_index:
                    left_index += 1
    return result

print(threeSum([-1,0,1,2-1,4]))


