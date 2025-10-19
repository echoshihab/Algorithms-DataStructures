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
        
        result = nums[0]
        curr_max = curr_min = 1

        for n in nums:
            vals = (n,  n * curr_max, n * curr_min)
            curr_max, curr_min = max(vals), min(vals)
            result = max(result, curr_max)
        
        return result
        


sol = Solution()
sol.maxProduct([2,3,-2,4])
