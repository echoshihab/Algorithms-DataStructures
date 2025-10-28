"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""

import bisect
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


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            if not res or num > res[-1]:
                res.append(num)
            else:
                idx = bisect.bisect_left(res,num)
                res[idx] = num

        return len(res)




class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        for n in nums:
            if not result or n > result[-1]:
                result.append(n)
            else:
                index = self.binarySearchLeft(result, n)
                result[index] = n
            
        return len(result)

    def binarySearchLeft(self, result, num):
        left, right = 0, len(result) - 1

        while left <= right:
            mid = (left + right) // 2
            if result[mid] < num:
                left = mid + 1
            else:
                right = mid - 1 
        return left
                        

class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result_dict = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    continue
                nums[i] = max(nums[i], 1 + nums[j])
        
        return max(result_dict)
                
                
        