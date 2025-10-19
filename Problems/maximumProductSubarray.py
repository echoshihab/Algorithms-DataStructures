"""Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer."""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        product = float('-inf')

        curr_product = nums[0]

        for i in range(1, len(nums)):
            temp = nums[i] * curr_product
            if temp < curr_product or temp < nums[i]:                
                curr_product = nums[i]
            else:
                curr_product = temp

            product = max(product, curr_product)
        
        

        return product
