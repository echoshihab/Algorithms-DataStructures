"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""

from collections import defaultdict
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = []
    postfix = [0] * len(nums)   
    result = []


    for i in range(0, len(nums)):
        if i > 0:
            prefix.append(prefix[i-1] * nums[i] )               
        else:
            prefix.append(nums[i])                           
        
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) - 1:
            postfix[i]=nums[i]
        else:
            postfix[i] = postfix[i+1] * nums[i]       
            
    for i in range(0, len(nums)):
         if i == 0:
            result.append(1 * postfix[i+1])
         elif i == len(nums) - 1:
            result.append(prefix[i-1] * 1)
         else:
            result.append(prefix[i-1] * postfix[i+1])

    return result


print(productExceptSelf([1,2,3,4]))


            


        